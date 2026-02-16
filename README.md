# X Mutual Follow Assistant

一个用于 **X（Twitter）互关活动** 的浏览器自动化技能（简体中文）。

核心流程固定：
1. 先处理上一条活动帖的回复（优先蓝V）
2. 按限额执行回关
3. 生成新文案并发布下一条活动帖
4. 保存新帖链接，供下次继续处理

---

## 最小安装（OpenClaw）

1. 把本目录放到你的 skills 目录（示例）：
   - `~/.agents/skills/x-mutual-follow-assistant/`
2. 创建运行配置文件：
   - 复制 `runtime-config.example.json` 为 `runtime-config.json`
3. 在 OpenClaw 中执行：
   - `执行 x 互关技能`

> 依赖：
> - 可用的 OpenClaw `browser` 工具
> - 已登录的 X 账号（openclaw 浏览器 profile）

---

## 配置文件（runtime-config.json）

关键字段：
- `targetMode`: `community` 或 `home`
- `communityUrl`: 当 `targetMode=community` 时必填
- `imagePaths`: 图片本地路径数组（可空）
- `rateLimit.maxFollows / perMinutes`: 回关限额
- `whitelist / blacklist`: 白名单/黑名单
- `state.lastPostUrl`: 上一条活动帖 URL

---

## 使用方式

### 1) 预览模式（不发帖、不回关）
让代理先给你：
- 本轮将处理的上一条帖子
- 预计回关计划
- 新文案草稿

### 2) 执行模式（正式跑）
让代理执行完整流程：
- 先处理上一条回复并回关
- 再发布新帖
- 最后更新 `state.lastPostUrl`

---

## 运行结果（建议输出）

每次运行都应包含：
- 已处理的上一条帖子 URL
- 识别到的蓝V候选数
- 本轮已回关数量
- 因限额延期数量
- 新发布帖子 URL
- 本轮 token 消耗（可估算）

---

## 边界与降级策略

- 图片路径失效：本轮自动降级为纯文案发帖，并提示你补发正确图片路径
- 不回显底层报错：只输出业务结论（发生了什么/影响是什么/下一步）
- 严格限速：避免突发批量操作

---

## GitHub 公开发布（最小步骤）

在本目录执行：

```bash
git init
git add .
git commit -m "feat: init x mutual follow assistant"
gh repo create x-mutual-follow-assistant --public --source . --remote origin --push
```

发布后仓库地址形如：
- `https://github.com/<你的用户名>/x-mutual-follow-assistant`
