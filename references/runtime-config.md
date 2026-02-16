# Runtime Config Schema

Use this schema to persist workflow settings.

```json
{
  "targetMode": "community | home",
  "communityUrl": "https://x.com/i/communities/... (required when targetMode=community)",
  "imagePaths": ["~/Downloads/file1.png", "~/Downloads/file2.png"],
  "rateLimit": {
    "maxFollows": 20,
    "perMinutes": 60
  },
  "whitelist": ["@trusted1", "@trusted2"],
  "blacklist": ["@spam1", "pattern:airdrop", "pattern:nsfw"],
  "schedule": {
    "pollRepliesEveryMinutes": 15,
    "followRunEveryMinutes": 30
  },
  "state": {
    "lastPostUrl": "",
    "processedUsers": [],
    "followQueue": []
  }
}
```

## Validation Rules
- `communityUrl` must be present if `targetMode=community`.
- `imagePaths` may be empty for text-only posts.
- `maxFollows` must be > 0.
- `perMinutes` should be >= 15.
- `blacklist` and `whitelist` should be deduplicated.
