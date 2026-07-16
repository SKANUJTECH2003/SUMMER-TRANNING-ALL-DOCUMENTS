from pathlib import Path
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

script_dir = Path(__file__).resolve().parent
image_path = script_dir / "image1.jpg"

if not image_path.exists():
    raise FileNotFoundError(f"Image not found: {image_path}")

img = Image.open(image_path).convert("RGB")
arr = np.array(img, dtype=np.int16)
mid_h, mid_w = arr.shape[0] // 2, arr.shape[1] // 2

regions = [
    (0, 90, 0, mid_h, 0, mid_w),
    (1, 90, 0, mid_h, mid_w, arr.shape[1]),
    (2, 90, mid_h, arr.shape[0], 0, mid_w),
    (None, None, mid_h, arr.shape[0], mid_w, arr.shape[1]),
]

out = arr.copy()
for channel, amount, top, bottom, left, right in regions:
    if channel is None:
        out[top:bottom, left:right] = np.clip(
            out[top:bottom, left:right] + [40, 40, 0], 0, 255
        )
    else:
        out[top:bottom, left:right, channel] = np.clip(
            out[top:bottom, left:right, channel] + amount, 0, 255
        )

out = out.astype(np.uint8)
plt.imshow(out)
plt.axis("off")
plt.show()
