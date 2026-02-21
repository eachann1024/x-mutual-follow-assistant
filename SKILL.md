---
name: x-mutual-follow-assistant
description: "X 社区互关技能：发帖 + 回关 + 悬浮卡关注。默认一次性完整执行；用抽象的滚动/关注行为复用到各阶段。"
---

# X 互关技能（X Mutual Follow Assistant）

> 目标：在 X 上一次性完成 **发帖 + 回关 + 悬浮卡关注**（默认完整执行，除非用户明确跳过）。

## 重要原则（强制）
1. **默认每次完整执行**：发帖 + 回关 + 悬浮卡关注。
2. **滚动行为要抽象复用**：所有需要滚动的阶段都遵循同一套滚动循环。
3. **媒体自动读取**：默认从 `./public/` 扫描媒体并上传；不反复质疑用户是否放了媒体。
4. 遇到验证码/真人验证/登录要求：**停止自动化**，提示用户在 Chrome 手动完成后再继续；不尝试绕过。

## 运行依赖（执行实现）
- 使用 **agent-browser + CDP Chrome（9222）** 执行（不依赖 X API）。
- 不再使用 `X_MUTUAL_FOLLOW_BROWSER_PROFILE=openclaw` 等旧 profile 环境变量。

---

## 1) 持久化配置（runtime-config.json）
- 配置模板：`runtime-config.example.json`
- 实际生效配置：`runtime-config.json`（**用户本地持久化**；允许长期修改，且不入库）
- 可选本地环境变量：`.env`（不入库；可从 `.env.example` 复制）

> 规则：
> - 用户说“以后都这样”→ 写回 `runtime-config.json`
> - 用户说“仅本次”→ 不写回

建议新增/使用的字段（示例见 `runtime-config.example.json`）：
- `followBackScrollPages`：回关滚动页数（默认 4）
- `hoverCardScrollPages`：社区页悬浮卡关注滚动页数（默认 6）
- `hoverCardMaxFollowsTotal`：悬浮卡阶段最多关注数（默认 30；0 表示不限制）
- `delayMsRange.min/max`：点击节奏（默认 500-700ms）
- `communityUrl`：社区来源 URL（默认已预置）
- `state.lastPostUrl`：上一条发帖 URL（用于下轮引用；执行后必须更新）

---

## 2) 通用行为抽象（核心）

### 2.1 ScrollLoop（滚动循环）
用于所有需要“滚动分页”的阶段。

参数：
- `pages`：滚动轮数（例如 4 / 6）
- `perPageAction()`：每一轮在当前视窗要执行的动作

统一流程：
1. 执行 `perPageAction()`（在当前视窗处理）
2. 随机等待 `delayMsRange`
3. 向下滚动一屏（建议 1200-1800px）
4. 等待 1-2 秒用于加载

> 这就是你说的“滚动一次关注一次再滚动”的抽象：**滚到一页 → 做关注动作 → 再滚**。

### 2.2 FollowInViewport（当前视窗关注）
在当前视窗内，**尽可能**点击所有可点击的 `Follow/关注` 按钮：
- 跳过 `Following/正在关注`
- 禁止打开个人主页（只点按钮）
- 出现风控/验证提示（关注上限/暂时无法关注/验证码/真人验证/手动登录）→ 立即停止并记录

---

## 3) 阶段 A：发帖（post）

### 3.1 媒体来源：默认 public/
- 自动扫描 `./public/` 并上传全部媒体。
- 支持格式（括号标注）：
  - 图片（`.png` / `.jpg` / `.jpeg` / `.gif` / `.webp`）
  - 视频（`.mp4` / `.mov` / `.webm`）
- **不反复确认用户有没有媒体**。
- 若扫描为 0：不阻塞，自动改为纯文本发帖；执行结束在报告里告知“未检测到媒体（public 为空或被删除）”。

### 3.2 发帖成功凭证（避免“URL 为空”）
- 发帖完成后必须尽量拿到“新发帖 URL”。
- 并写入 `runtime-config.json` 的 `state.lastPostUrl`（下次执行会用）。

---

## 4) 阶段 B：回关（followBack）
目标页：`https://x.com/each1024/following`

参数：
- `pages = followBackScrollPages`（默认 4）

执行：
- 使用 `ScrollLoop(pages)`
- `perPageAction = FollowInViewport()`

含义：
- **滚动 4 页**
- **每页把当前视窗里能回关的都回关完**，再滚到下一页

---

## 5) 阶段 C：社区页悬浮卡关注（hoverCardFollow）
入口：`<communityUrl>/retweets/with_comments`

参数：
- `pages = hoverCardScrollPages`（默认 6）
- `maxTotal = hoverCardMaxFollowsTotal`（默认 30；0=不限制）

执行：
- 使用 `ScrollLoop(pages)`
- 每页 perPageAction：
  1) 获取当前页作者列表（优先轻量提取，必要时 snapshot）
  2) 对每个作者：hover 触发悬浮卡 → 找 `Follow/关注` 点击
  3) 不打开作者主页
  4) 达到 `maxTotal` 立即停止

---

## 6) 执行前知情清单（必须确认）
开始任何浏览器动作前，先发给用户一份清单并等待确认：
- 是否完整执行三阶段（默认全开）
- 回关页数（followBackScrollPages）
- 悬浮卡页数（hoverCardScrollPages）+ 总关注上限（hoverCardMaxFollowsTotal）
- 节奏（delayMsRange）
- public 媒体数量（自动扫描得出；为 0 也会继续）
- 风控风险（可能出现验证码/真人验证需用户手动处理）

---

## 7) 输出报告（简版）
至少包含：
- communityUrl
- 发帖是否成功（URL/截图其一）+ 媒体数量（若 0 说明原因）
- 回关：滚动页数 + 关注数量（可分页）
- 悬浮卡：滚动页数 + 关注数量（说明是否触达上限）
- 是否触发风控/验证
- 本次是否改动配置（默认不改；如改需列出字段与新值）

---

## 维护说明
- 仓库默认只保留执行所需文档与模板；不再保留未被当前流程使用的辅助脚本/参考资料目录。
