---
name: x-mutual-follow-assistant
description: Run a browser-only X mutual-follow workflow in Simplified Chinese. Use when the user wants to (1) revisit the previous campaign post, process blue-V reply follow-backs with rate limits and blacklist/whitelist filters, then (2) publish a new campaign post to community or home feed with optional images and fresh copy each run.
---

# X Mutual Follow Assistant

Publish and maintain X “mutual follow” campaigns with safe pacing and repeatable operations.

## Workflow (browser-only, fixed order)

1. Collect required inputs on first run.
2. Open previous post URL from local state.
3. Scan replies, prioritize 蓝V, and execute follow-backs with rate limits.
4. Generate fresh Simplified Chinese post copy with emoji.
5. Publish the new post to community or home feed.
6. Save new post URL as next run's previous post.
7. Report outcomes + token usage summary.

## Step 1 — First-Run Intake (must ask)

Ask these questions before the first execution in a session:

1. Need images or text-only?
   - If images are needed, collect one or more local paths such as `~/Downloads/fileName.png`.
2. Post target?
   - `community`: require community URL (example: `https://x.com/i/communities/1669241668829323264`)
   - `home`: publish on profile/home feed.
3. Rate limit?
   - Collect max follows per time window (example: 20 per hour).
4. Optional allow/deny rules?
   - Whitelist handles (always prioritize)
   - Blacklist handles/patterns (always skip)

Reuse saved answers unless the user asks to change them.

## Step 2 — Copy Generation Rules

Generate in Simplified Chinese. Keep meaning stable, wording new every run.

Core meaning to preserve:
- If the replier is 蓝V and replies anything under the post, the account will be followed back on schedule.

Rules:
- Produce new phrasing each run (change opening, CTA, emoji mix, line breaks).
- Keep tone clear and friendly, not spammy.
- Include a direct action prompt (reply + follow).
- Keep it concise and readable on mobile.
- Do not claim instant follow-back; say scheduled/periodic follow-back.

Load style examples from `references/copy-guidelines.md` when generating content.

## Step 3 — Process Previous Post First

Use browser automation to open `state.lastPostUrl` from runtime state.

- If no previous post exists, skip follow-back and go to publishing.
- Scan replies under that post.
- Prioritize 蓝V accounts.
- Require at least one visible reply on the tracked post.
- Skip already-followed or already-processed accounts.
- Apply whitelist/blacklist before queueing.

## Step 4 — Safe Follow Execution

Apply strict pacing on queued candidates:

- Respect configured limit `N / window` (for example: 20/hour).
- Run in small batches, not burst mode.
- Stop at limit and defer the rest to next cycle.
- Record failures and retry with capped retries.

## Step 5 — Publish New Post After Follow-Back

- Generate fresh copy for this run.
- If target is `community`, post to the provided community URL.
- If target is `home`, post on home feed.
- If images are configured, attach selected files.
- Save the newly published post URL to `state.lastPostUrl`.

## Step 6 — Output Format

Return concise business-facing status:

- Previous post URL processed
- Blue-V candidates detected
- Follows executed this run
- Deferred by rate limit
- New post URL published
- Token usage summary for this run (must include estimated/actual token count when available)

User-facing style constraints (mandatory):
- Never expose raw tool/terminal errors (no `Exec:` / stack trace / command dump in user chat).
- Convert failures into plain-language conclusion: what happened → impact → next action.
- If image upload/path fails, continue in text-only mode for current run **and** explicitly ask user to resend valid local image path(s) for next run.
- Always end with one clear next step the user can act on.

## Browser Execution Rules

- Use browser automation as the only execution path (no API dependency).
- Use OpenClaw browser profile `openclaw` for X operations.
- Keep one tracked post URL in runtime state so the next run always starts from the previous post.

## Modes

- Preview mode: show previous-post processing plan + fresh copy draft + target, do not post/follow.
- Execute mode: process previous post follow-backs first, then publish new post, then persist state.

## Resources

- Copy examples and rewrite patterns: `references/copy-guidelines.md`
- Runtime config schema: `references/runtime-config.md`
- Optional local helper for fresh copy drafts: `scripts/generate_copy.py`
