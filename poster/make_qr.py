#!/usr/bin/env python3
"""Generate a styled QR code with a centered text label.

Usage:
    python make_qr.py <data> <label> <output.png>

Examples:
    python make_qr.py "mailto:rickard.brannvall@ri.se" mailto qr_email.png
    python make_qr.py "https://rickardbrannvall.github.io/poster/LeakProPitch" poster qr_LeakProPitch.png

The QR code is version 6 (41 data modules), high error correction,
10px per module, 4-module quiet zone border => 490x490 px output.

The label sits in a centered box with:
  - 1-module black border
  - 1-module inner perimeter with ~35% randomly scattered black pixels
  - 1-module gap to the text area
Box spans modules 18-30 (w) x 20-28 (h) of the 49-module grid.
"""

import sys
import random
import qrcode
from PIL import Image, ImageDraw, ImageFont

MODULE = 10
VERSION = 6
BORDER = 4
SCATTER_PROB = 0.35


def make_qr(data: str, label: str, output: str):
    qr = qrcode.QRCode(
        version=VERSION,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=MODULE,
        border=BORDER,
    )
    qr.add_data(data)
    qr.make(fit=False)

    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    draw = ImageDraw.Draw(img)

    # Box position (in modules): cols 18-30, rows 20-28
    bx1, by1 = 18 * MODULE, 20 * MODULE
    bx2, by2 = 31 * MODULE, 29 * MODULE

    # Black border
    draw.rectangle([bx1, by1, bx2 - 1, by2 - 1], fill="black")

    # White interior
    ix1, iy1 = bx1 + MODULE, by1 + MODULE
    ix2, iy2 = bx2 - MODULE, by2 - MODULE
    draw.rectangle([ix1, iy1, ix2 - 1, iy2 - 1], fill="white")

    # Scattered pixels along inside perimeter
    positions = []
    for x in range(ix1, ix2, MODULE):
        positions.append((x, iy1))
        positions.append((x, iy2 - MODULE))
    for y in range(iy1 + MODULE, iy2 - MODULE, MODULE):
        positions.append((ix1, y))
        positions.append((ix2 - MODULE, y))

    for px, py in positions:
        if random.random() < SCATTER_PROB:
            draw.rectangle([px, py, px + MODULE - 1, py + MODULE - 1], fill="black")

    # Centered label text
    try:
        font = ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16
        )
    except OSError:
        font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), label, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    cx, cy = (bx1 + bx2) // 2, (by1 + by2) // 2
    draw.text((cx - tw // 2, cy - th // 2), label, fill="black", font=font)

    img.save(output)
    print(f"Saved {output} ({img.size[0]}x{img.size[1]})")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(__doc__)
        sys.exit(1)
    make_qr(sys.argv[1], sys.argv[2], sys.argv[3])
