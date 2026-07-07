from pathlib import Path
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Open and ensure RGB mode
script_dir = Path(__file__).resolve().parent
image_path = script_dir / "image1.jpg"

if not image_path.exists():
    raise FileNotFoundError(f"Image not found: {image_path}")

img = Image.open(image_path).convert("RGB")
arr = np.array(img, dtype=np.int16)

# Increase red channel and convert back to uint8
arr[:, :, 0] = np.clip(arr[:, :, 0] + 90, 0, 155)
arr = arr.astype(np.uint8)

plt.imshow(arr)
plt.axis("off")
plt.show()