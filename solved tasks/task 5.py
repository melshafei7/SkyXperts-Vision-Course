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

# Crop the image
cropped = img[20:200, 50:200]

# Display original and cropped images
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(cv.cvtColor(cropped, cv.COLOR_BGR2RGB))
plt.title("Cropped Image")
plt.axis("off")

plt.tight_layout()
plt.show()