import cv2 as cv
import matplotlib.pyplot as plt
import sys

# Load image in BGR
path = r"C:\Users\ASUS\OneDrive\Desktop\skyexperts tasks\task 1\beautiful-natural-image-1844362_1280.jpg"

img_bgr = cv.imread(path)

# Check if image was loaded successfully
if img_bgr is None:
    print("Error: Could not read the image.")
    sys.exit()

# Convert to different color spaces
img_rgb = cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB)
img_hsv = cv.cvtColor(img_bgr, cv.COLOR_BGR2HSV)
img_lab = cv.cvtColor(img_bgr, cv.COLOR_BGR2LAB)
img_gray = cv.cvtColor(img_bgr, cv.COLOR_BGR2GRAY)

# Display all images
plt.figure(figsize=(15, 10))

# BGR
plt.subplot(2, 3, 1)
plt.imshow(img_bgr)
plt.title("BGR")
plt.axis("off")

# RGB
plt.subplot(2, 3, 2)
plt.imshow(img_rgb)
plt.title("RGB")
plt.axis("off")

# HSV
plt.subplot(2, 3, 3)
plt.imshow(img_hsv)
plt.title("HSV")
plt.axis("off")

# LAB
plt.subplot(2, 3, 4)
plt.imshow(img_lab)
plt.title("LAB")
plt.axis("off")

# Grayscale
plt.subplot(2, 3, 5)
plt.imshow(img_gray, cmap="gray")
plt.title("Grayscale")
plt.axis("off")

plt.tight_layout()
plt.show()