# X 互关技能（OpenClaw）

## 给用户看的最简使用教程（放顶部）

### 1）先安装技能
在 Telegram 发：

```text
帮我安装 https://github.com/eachann1024/x-mutual-follow-assistant 这个技能
```

### 2）安装后让 OpenClaw 定时跑
在 Telegram 发：

```text
帮我定时执行，每天执行两次，分别是下午 1:30 和下午 6:30
```

OpenClaw 首次会这样问你（固定 5 项）：

```text
我现在就能执行。先给我这 4 个值（首次必填），我拿到后会持久化保存到技能中：
1. 发帖位置：社区 还是 首页
2. 如果是社区：发帖链接（例如 https://x.com/i/communities/...）
3. 要不要配图：不要 / 要（要的话给图片路径，如 ~/Downloads/a.png）
4. 回关限频（可选默认 20）：例如“每小时最多 20 人”
5. 在 openclaw 的浏览器中登录 X（不阻塞）
你回复这四项后，我直接开始执行并回报结果 + 本次 token 消耗。
```

你的回复示例：

```text
1 社区
2 https://x.com/i/communities/1669241668829323264
3 配图，图片地址是：~/Desktop/x.jpeg
4 每小时最多 20 人
```

---

## 给机器人（OpenClaw）看的最小安装说明

1. 拉取仓库到本机（建议放 `~/Work/`）
2. 将技能目录放到 OpenClaw skills 路径
3. 复制 `runtime-config.example.json` 为 `runtime-config.json`
4. 在 OpenClaw 浏览器（`profile=openclaw`）中登录 X
5. 执行：`执行 x 互关技能`

---

## 持久化说明（/new 后仍保留）

- 运行配置/状态：`runtime-config.json`
- 技能执行规则：`SKILL.md`

只要这两个文件还在，`/new` 后也会继续按原配置执行。

---

## 输出标准（每次执行后）

必须返回：
- 处理的上一条帖子 URL
- 蓝V候选数
- 本轮回关数
- 限频延期数
- 新帖子 URL
- 本次 token 消耗

如果图片路径失效：
- 本轮自动降级纯文案
- 同时明确引导用户补发正确图片路径
