"""Copy the pre-built entry image to the output directory.

The image (entry.png, 1024x1024) is drawn at build time from a
text-free illustration plus PIL-rendered labels; this program only
places it where the grader expects it, deterministically.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main():
    src = HERE / "entry.png"
    data = src.read_bytes()
    if not data.startswith(PNG_MAGIC):
        raise ValueError("entry.png is not a valid PNG")
    if len(data) > 1_048_576:
        raise ValueError("entry.png exceeds the 1 MiB limit")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out_dir / "entry.png")


if __name__ == "__main__":
    main()
