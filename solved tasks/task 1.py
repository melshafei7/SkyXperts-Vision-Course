import cv2 as cv
import numpy as np
import sys
import matplotlib.pyplot as plt

# Your code here
path = r'"C:\Users\ASUS\OneDrive\Desktop\skyexperts tasks\task 1\beautiful-natural-image-1844362_1280.jpg"'  # Replace with your image path

# Read in BGR
img_bgr = cv.imread(path, cv.IMREAD_COLOR)
# Read in Grayscale
img_gray = cv.imread(path, cv.IMREAD_GRAYSCALE)

# Handle errors if image cannot be read
if img_bgr is None or img_gray is None:
    print("Error: Could not read the image.")
    sys.exit()

# Display both using cv.imshow() or plt.imshow()
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB))
plt.title("BGR Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(img_gray, cmap="gray")
plt.title("Grayscale Image")
plt.axis("off")

plt.show()