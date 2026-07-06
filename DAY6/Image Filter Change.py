import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Open and ensure RGB mode
img = Image.open("image1.jpg").convert("RGB")
arr = np.array(img, dtype=np.int16)

# Increase red channel and convert back to uint8
arr[:, :, 0] = np.clip(arr[:, :, 0] + 90, 0, 155)
arr = arr.astype(np.uint8)

plt.imshow(arr)
plt.axis("off")
plt.show()