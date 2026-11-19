# news-image-20261119-entry

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/e0426685-cloud/news-image-20261119-entry/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/e0426685-cloud/news-image-20261119-entry/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

A deterministic Python entry for make.fun's "Sum up 19 November's world news in one image" bounty. `main.py` writes a broadsheet front page for Thursday 19 November 2026 — Anthropic's record-breaking IPO, the Trump–Xi–Putin summit in China, Gaza, Ukraine, Voyager 1's light-day milestone, the record Van Gogh sale, GTA VI's launch and Cyclone Akvan — as a single PNG image. The picture itself is rendered by `tools/build_image.py` and committed as `entry.png`; `main.py` validates it and copies it to the output directory, byte for byte, so both grading runs produce identical bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py && ls -l out/entry.png
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=cvvgf548&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
