import cv2 as cv
import matplotlib.pyplot as plt
import sys

# Load image
path = r"C:\Users\ASUS\OneDrive\Desktop\skyexperts tasks\task 1\beautiful-natural-image-1844362_1280.jpg"

img = cv.imread(path)

# Check if image was loaded successfully
if img is None:
    print("Error: Could not read the image.")
    sys.exit()

# Downscale to 60%
downscaled = cv.resize(
    img,
    None,
    fx=0.6,
    fy=0.6,
    interpolation=cv.INTER_AREA
)

# Upscale to 200%
upscaled = cv.resize(
    img,
    None,
    fx=2.0,
    fy=2.0,
    interpolation=cv.INTER_CUBIC
)

# Compare shapes
print("Original shape:", img.shape)
print("60% shape:", downscaled.shape)
print("200% shape:", upscaled.shape)

# Display all three
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.title(f"Original\n{img.shape}")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(cv.cvtColor(downscaled, cv.COLOR_BGR2RGB))
plt.title(f"Downscaled 60%\n{downscaled.shape}")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(cv.cvtColor(upscaled, cv.COLOR_BGR2RGB))
plt.title(f"Upscaled 200%\n{upscaled.shape}")
plt.axis("off")

plt.tight_layout()
plt.show()