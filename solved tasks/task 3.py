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

# Get original dimensions
height, width = img.shape[:2]

# Resize only width to 100 pixels (keep original height)
width_100 = cv.resize(img, (100, height))

# Resize only height to 200 pixels (keep original width)
height_200 = cv.resize(img, (width, 200))

# Resize both width and height to 200 x 200
both_200 = cv.resize(img, (200, 200))

# Print shapes
print("Original shape:", img.shape)
print("Width = 100:", width_100.shape)
print("Height = 200:", height_200.shape)
print("200 x 200:", both_200.shape)

# Display all images
plt.figure(figsize=(16, 5))

plt.subplot(1, 4, 1)
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.title("Original")
plt.axis("off")

plt.subplot(1, 4, 2)
plt.imshow(cv.cvtColor(width_100, cv.COLOR_BGR2RGB))
plt.title("Width = 100")
plt.axis("off")

plt.subplot(1, 4, 3)
plt.imshow(cv.cvtColor(height_200, cv.COLOR_BGR2RGB))
plt.title("Height = 200")
plt.axis("off")

plt.subplot(1, 4, 4)
plt.imshow(cv.cvtColor(both_200, cv.COLOR_BGR2RGB))
plt.title("200 x 200")
plt.axis("off")

plt.tight_layout()
plt.show()