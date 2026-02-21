# Runtime Config Schema（运行时配置）

> `runtime-config.json`：用户本地持久化配置（可长期修改）
> 
> `runtime-config.example.json`：仓库内模板。

```json
{
  "communityUrl": "https://x.com/virtuals_io/status/...",

  "followBackScrollPages": 4,
  "hoverCardScrollPages": 6,
  "hoverCardMaxFollowsTotal": 30,

  "delayMsRange": { "min": 500, "max": 700 },

  "enableStages": {
    "post": true,
    "followBack": true,
    "hoverCardFollow": true
  },

  "state": {
    "lastPostUrl": ""
  }
}
```

## Validation Rules
- `communityUrl` 必须是一个可访问的 X 帖子 URL。
- `followBackScrollPages` / `hoverCardScrollPages` 建议 >= 1。
- `hoverCardMaxFollowsTotal`：0 表示不限制；否则建议 1-200。
- `delayMsRange.min/max`：建议 200ms 以上，避免过猛触发风控。
