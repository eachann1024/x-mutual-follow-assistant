#!/usr/bin/env python3
"""Generate fresh Simplified Chinese mutual-follow copy for X posts."""

from __future__ import annotations

import argparse
import random
import time

OPENERS = [
    "🤝 蓝V互关计划开启",
    "✅ 蓝V朋友看这里",
    "🌟 想互关的蓝V请集合",
    "🚀 蓝V互关小活动",
    "📌 这条给蓝V朋友",
]

CONDITIONS = [
    "在这条帖子下回复任意内容并关注我",
    "在本帖评论区留任意一句并先关注我",
    "在这里评论任意内容，再关注我",
    "在评论区随便回一句并关注我",
]

PROMISES = [
    "我会定时回关你。",
    "我会按计划分批回关。",
    "我会在固定时段回关。",
    "我会周期性处理并回关。",
]

CTAS = [
    "来留言，我会按节奏处理～",
    "现在就评论一条吧！",
    "评论区见，安排上。",
    "留个言就开始进入队列。",
]

EMOJIS = ["🚀", "🤝", "✅", "🔔", "⏰", "🌟", "💙", "📌", "🎯"]


def build_copy(seed: int | None = None) -> str:
    if seed is None:
        seed = time.time_ns()
    rnd = random.Random(seed)

    opener = rnd.choice(OPENERS)
    condition = rnd.choice(CONDITIONS)
    promise = rnd.choice(PROMISES)
    cta = rnd.choice(CTAS)
    emojis = " ".join(rnd.sample(EMOJIS, k=3))

    return f"{opener} {emojis}\n{condition}，{promise}\n{cta}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=None)
    args = parser.parse_args()
    print(build_copy(args.seed))
