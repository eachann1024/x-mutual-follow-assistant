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
- 当前实现以 **agent-browser + CDP** 为准，已不再使用 `X_MUTUAL_FOLLOW_BROWSER_PROFILE=openclaw` 这类旧变量。

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

## 6) 仓库瘦身说明
当前仓库仅保留执行必需文件；历史上的 `references/` 与 `scripts/` 辅助材料已移除，避免“文件存在但文档未引用”。
