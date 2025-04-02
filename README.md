# SmartBar
[![PyPI](https://static.pepy.tech/badge/smartbar)](https://pypi.org/project/smartbar/)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repo-black?logo=github)](https://github.com/lama2923/smartbar)

**SmartBar** is a powerful, automatic, and extensible progress bar library for Python, built with smart I/O tracking and multi-threading support.  
It provides real-time progress, ETA, speed tracking, and works seamlessly with file and network I/O using `with` blocks — no manual `.update()` needed.

---

## Features

- [x] Thread-safe and supports concurrent usage  
- [x] Supports multiple bars simultaneously  
- [x] Automatically wraps `open()`, `requests.get()`, and `aiohttp`  
- [x] Tracks both reading and writing operations  
- [x] Smart speed and ETA calculation (combines recent + average)  
- [x] Fully customizable output and bar style  
- [x] Pause, resume, ignore, and manual update support  
- [x] Works with `with` and `async with` contexts  

---

## Installation

```bash
pip install smartbar
```

---

## Basic Example

```python
from smartbar import SmartBar
import requests

with SmartBar("Downloading", length=40) as bar:
    r = requests.get("https://example.com/file", stream=True)
    for chunk in r.iter_content(1024):
        pass  # progress is auto-tracked
```

---

## Custom Style & Live Animation

```python
from smartbar import SmartBar
import requests
import time

BAR1 = "%(DESC). \033[48;5;214m[%(BAR)]\033[0m %(CUR)/%(TOTAL) (%(PERCENT)) | %(SPEED) | ETA: %(ETA)"
BAR2 = "%(DESC).. \033[48;5;214m[%(BAR)]\033[0m %(CUR)/%(TOTAL) (%(PERCENT)) | %(SPEED) | ETA: %(ETA)"
BAR3 = "%(DESC)... \033[48;5;214m[%(BAR)]\033[0m %(CUR)/%(TOTAL) (%(PERCENT)) | %(SPEED) | ETA: %(ETA)"

url = "https://download.samplelib.com/mp4/sample-20s.mp4"

with SmartBar("Downloading", custom_bar_output=BAR1) as bar:
    response = requests.get(url, stream=True)
    with open("video.mp4", "wb") as f:
        stime = time.time()
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
            if time.time() - stime > 1:
                # Animate bar every second
                bar.custom_bar_output = BAR2 if bar.custom_bar_output == BAR1 else (
                    BAR3 if bar.custom_bar_output == BAR2 else BAR1
                )
                stime = time.time()
```

---

## Manual Progress (Disable Auto Tracking)

```python
import time
from smartbar import SmartBar

BAR1 = "%(DESC). {} SEC \033[48;5;214m[%(BAR)]\033[0m %(CUR)/%(TOTAL) (%(PERCENT)) | %(SPEED) | ETA: %(ETA)"
BAR2 = "%(DESC).. {} SEC \033[48;5;214m[%(BAR)]\033[0m %(CUR)/%(TOTAL) (%(PERCENT)) | %(SPEED) | ETA: %(ETA)"
BAR3 = "%(DESC)... {} SEC \033[48;5;214m[%(BAR)]\033[0m %(CUR)/%(TOTAL) (%(PERCENT)) | %(SPEED) | ETA: %(ETA)"

SEC = 10

with SmartBar("Waiting", auto_bar=False, mode="items") as bar:
    bar.total = SEC
    start = time.time()
    last = time.time()
    while True:
        now = time.time()
        if now - last > 1:
            elapsed = int(now - start)
            seconds_left = max(0, SEC - elapsed)

            if bar.custom_bar_output == BAR1:
                bar.custom_bar_output = BAR2.format(seconds_left)
            elif bar.custom_bar_output == BAR2:
                bar.custom_bar_output = BAR3.format(seconds_left)
            else:
                bar.custom_bar_output = BAR1.format(seconds_left)

            bar.add(now - last)
            last = now

        if bar.current >= bar.total:
            break
```

---

## Async Support

```python
import aiohttp
import asyncio
from smartbar import SmartBar

async def download():
    async with SmartBar("Async Download") as bar:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://example.com") as resp:
                async for chunk in resp.content.iter_chunked(1024):
                    pass  # progress auto-tracked

asyncio.run(download())
```

---

## Pause, Resume & Ignore

```python
from smartbar import SmartBar
import requests

with SmartBar("Download") as bar:
    r = requests.get("https://example.com/file", stream=True)

    bar.pause()
    # Do something non-tracked...
    bar.resume()

    bar.ignore(r)  # disables tracking for this object
```

---

## Format Variables

You can customize the output bar using these placeholders:

| Placeholder  | Meaning                    |
|--------------|----------------------------|
| `%(DESC)`    | Bar description            |
| `%(BAR)`     | The visual progress bar    |
| `%(CUR)`     | Current value              |
| `%(TOTAL)`   | Total expected value       |
| `%(PERCENT)` | Percentage completed       |
| `%(SPEED)`   | Transfer speed             |
| `%(ETA)`     | Estimated time remaining   |

Example:  
`"%(BAR)"` → `[#######.......]`


## bar_style
```python
with SmartBar("Waiting", auto_bar=False, mode="items", bar_style="simple", style=r"——") as bar: 
    pass
```

## custom_bar_style
```python
example_style = {  # [Foreground, Background]
    "BAR": {
        "+": [0xFFFFFF, 0x000000],
        "-": [0x888888, None],
    },
    "DESC": [0xAAAAAA, None],
    "CUR": [0xAAAAAA, None],
    "TOTAL": [0xAAAAAA, None],
    "PERCENT": [0xAAAAAA, None],
    "SPEED": [0xAAAAAA, None],
    "ETA": [0xAAAAAA, None],
}

with SmartBar("Waiting", auto_bar=False, mode="items", custom_bar_style=example_style, style=r"——") as bar:
    pass
```

---

## License

MIT

---

## Author

**lama2923**  
GitHub: [https://github.com/lama2923](https://github.com/lama2923)