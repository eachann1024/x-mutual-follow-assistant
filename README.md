# x-mutual-follow-assistant（X 互关技能）

这是一个用于 X 的互关辅助技能：默认一次性完整执行 **发帖 + 回关 + 悬浮卡关注**。

## 1) 安装
把本仓库放到你的全局 skills 目录（OpenClaw 自动发现）：

`~/.agents/skills/x-mutual-follow-assistant/`

> 建议：全局技能才是单一真相（不要在工作区放第二份副本）。

## 2) 配置（本地文件策略）
复制配置模板：

- `runtime-config.example.json` → `runtime-config.json`

本地文件说明：
- `runtime-config.json`：本地持久化配置，**不入库**（仓库只保留模板）。
- `.env`：可选本地覆盖项，**不入库**；如需可从 `.env.example` 复制。

### Browser Backend（环境无关）
本技能不绑定特定浏览器/插件/profile。你只需要能在**任意浏览器**登录 X。

`runtime-config.json` 可配置自动化后端：
- `browserBackend`: `"auto" | "cdp" | "playwright" | "openclaw-browser-relay"`
  - 默认 `auto`：按当前环境自动选择最可用的执行通道。
- `cdpPort`: CDP 端口（可选，默认 `9222`）。
- `browserProfile`: **可选**，仅在你确实需要指定 profile 时再加，不是必填。

自动化通道可多选：CDP、Playwright、OpenClaw Browser Relay 等；不要求必须安装某个插件。

常用字段：
- `communityUrl`
- `followBackScrollPages`（回关页数，默认 4）
- `hoverCardScrollPages`（悬浮卡页数，默认 6）
- `hoverCardMaxFollowsTotal`（悬浮卡最多关注数，默认 30；0=不限制）
- `delayMsRange`（默认 500-700ms）

## 3) 发帖素材放哪里？支持什么格式？
把要发送的素材丢到：

`public/`

- 支持格式（括号标注）：
  - 图片（`.png` / `.jpg` / `.jpeg` / `.gif` / `.webp`）
  - 视频（`.mp4` / `.mov` / `.webm`）
- 会自动扫描并**全部上传**（多个就传多个）。
- 不会反复问你“有没有放素材”。
- 如果你手动删空了导致目录为空：不会阻塞执行，会改为纯文本继续；执行完会告知本次未检测到媒体。

不知道放什么？可以放：自我介绍短视频 / 作品演示 / 产品截图 / 项目封面 / 成果截图。

## 4) “滚动行为”是什么？
所有需要滚动的阶段都遵循同一抽象：

- **滚到一页 → 做关注动作（尽量把当前视窗能点的都点完）→ 再滚**

回关阶段：默认 4 页。
悬浮卡阶段：默认 6 页，可设置关注总上限。

## 5) 执行
在聊天里说：

`执行 x 互关技能`

执行前会先给你“执行知情清单”（阶段开关、页数、节奏、素材数量、风控风险），你确认后才会开始。

> 遇到验证码/真人验证/登录校验时，需要你手动处理，处理完成后再继续自动化。

## 6) 仓库瘦身说明
当前仓库仅保留执行必需文件；历史上的 `references/` 与 `scripts/` 辅助材料已移除，避免“文件存在但文档未引用”。
