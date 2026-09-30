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

# Calculate midpoints for height and width
height, width = img.shape[:2]

mid_h = height // 2
mid_w = width // 2

# Crop into top-left, top-right, bottom-left, bottom-right
top_left = img[:mid_h, :mid_w]
top_right = img[:mid_h, mid_w:]
bottom_left = img[mid_h:, :mid_w]
bottom_right = img[mid_h:, mid_w:]

# Display each block
plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.imshow(cv.cvtColor(top_left, cv.COLOR_BGR2RGB))
plt.title("Top Left")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(cv.cvtColor(top_right, cv.COLOR_BGR2RGB))
plt.title("Top Right")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(cv.cvtColor(bottom_left, cv.COLOR_BGR2RGB))
plt.title("Bottom Left")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(cv.cvtColor(bottom_right, cv.COLOR_BGR2RGB))
plt.title("Bottom Right")
plt.axis("off")

plt.tight_layout()
plt.show()

# Stitch back using NumPy
top_row = np.hstack((top_left, top_right))
bottom_row = np.hstack((bottom_left, bottom_right))

stitched = np.vstack((top_row, bottom_row))

# Display stitched image
plt.figure(figsize=(8, 6))
plt.imshow(cv.cvtColor(stitched, cv.COLOR_BGR2RGB))
plt.title("Stitched Image")
plt.axis("off")
plt.show()

# Verify
print("Original shape:", img.shape)
print("Stitched shape:", stitched.shape)
print("Images are identical:", np.array_equal(img, stitched))