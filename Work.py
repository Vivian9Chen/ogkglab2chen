"""
Usage:
  python render_points.py DS5.txt result.png
"""

import re
import sys
from PIL import Image, ImageDraw

W, H = 960, 540

def read_points(path: str):
    pts = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = re.split(r"[,\s]+", line)
            if len(parts) < 2:
                continue
            try:
                x = int(parts[0])
                y = int(parts[1])
                pts.append((x, y))
            except ValueError:
                continue
    return pts

def main():
    if len(sys.argv) < 3:
        print("Usage: python render_points.py <dataset.txt> <output.png>")
        sys.exit(1)

    in_path = sys.argv[1]
    out_path = sys.argv[2]

    pts = read_points(in_path)

    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)

    r = 1  # робимо точку помітнішою (3x3 пікселі)
    skipped = 0

    for x, y in pts:
        if not (0 <= x < W and 0 <= y < H):
            skipped += 1
            continue

        x_img = x
        y_img = (H - 1) - y  # переворот осі Y

        draw.rectangle([x_img - r, y_img - r, x_img + r, y_img + r], fill="black")

    img.save(out_path)
    print(f"Saved: {out_path}")
    print(f"Points read: {len(pts)}, skipped(out of bounds): {skipped}")

if __name__ == "__main__":
    main()
