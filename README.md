# X 互关技能（OpenClaw）

## 使用方式（用户）

在 Telegram 里直接说：

```text
帮我安装 https://github.com/eachann1024/x-mutual-follow-assistant 这个技能
```

安装后再说：

```text
帮我定时执行，每天执行两次，分别是下午 1:30 和下午 6:30
```

首次执行时，机器人会确认：
- 发帖位置（社区 / 首页）
- 社区链接（发社区时需要）
- 是否配图（如要，提供本地图片路径）
- 回关限频（不填则使用默认值）
- 在 OpenClaw 浏览器中登录 X

示例回复：

```text
1 社区
2 https://x.com/i/communities/1669241668829323264
3 配图，图片地址是：~/Desktop/x.jpeg
4 每小时最多 20 人
```

---

## 安装说明（OpenClaw）

1. 将本技能放入**当前 OpenClaw 实例的 skills 目录**（使用你本机实例路径，不写死）。
2. 复制 `runtime-config.example.json` 为 `runtime-config.json`。
3. 在 OpenClaw 浏览器（`profile=openclaw`）登录 X。
4. 在聊天中执行：`执行 x 互关技能`。

---

## 持久化

- 运行配置与状态：`runtime-config.json`
- 技能规则：`SKILL.md`

只要这些文件还在，`/new` 后配置仍会保留。

---

## 每次执行的回报内容

- 处理的上一条帖子 URL
- 蓝V候选数量
- 本轮已回关数量
- 限频延期数量
- 新发布帖子 URL
- 本次 token 消耗

如果图片路径失效：
- 本轮自动降级为纯文案发布
- 同时提示补发可用图片路径
