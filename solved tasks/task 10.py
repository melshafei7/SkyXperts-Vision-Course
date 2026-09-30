import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import sys

# Load image
path = r"C:\Users\ASUS\OneDrive\Desktop\skyexperts tasks\task 1\beautiful-natural-image-1844362_1280.jpg"

img = cv.imread(path)

# Check if image was loaded successfully
if img is None:
    print("Error: Could not read the image.")
    sys.exit()

# Apply blur using a 5x5 kernel
blurred = cv.blur(img, (5, 5))

# Sharpening kernel - normal strength
kernel1 = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

# Sharpening kernel - stronger
kernel2 = np.array([
    [0, -2, 0],
    [-2, 9, -2],
    [0, -2, 0]
])

# Apply sharpening to the blurred image
sharpened1 = cv.filter2D(blurred, -1, kernel1)
sharpened2 = cv.filter2D(blurred, -1, kernel2)

# Display results
plt.figure(figsize=(16, 8))

plt.subplot(2, 2, 1)
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(cv.cvtColor(blurred, cv.COLOR_BGR2RGB))
plt.title("Blurred Image (5x5)")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(cv.cvtColor(sharpened1, cv.COLOR_BGR2RGB))
plt.title("Sharpened - Kernel 1")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(cv.cvtColor(sharpened2, cv.COLOR_BGR2RGB))
plt.title("Sharpened - Kernel 2 (Stronger)")
plt.axis("off")

plt.tight_layout()
plt.show()