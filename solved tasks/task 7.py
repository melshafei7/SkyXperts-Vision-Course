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

# Get image dimensions
height, width = img.shape[:2]

# Calculate center of the image
center = (width // 2, height // 2)

# Rotation angles
angles = [45, 90, 180]

# Store rotated images
rotated_images = []

# For each angle: get matrix and warp
for angle in angles:
    rotation_matrix = cv.getRotationMatrix2D(
        center,
        angle,
        1.0
    )

    rotated = cv.warpAffine(
        img,
        rotation_matrix,
        (width, height)
    )

    rotated_images.append(rotated)

# Display original and all rotations
plt.figure(figsize=(14, 10))

plt.subplot(2, 2, 1)
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

for i, angle in enumerate(angles):
    plt.subplot(2, 2, i + 2)
    plt.imshow(cv.cvtColor(rotated_images[i], cv.COLOR_BGR2RGB))
    plt.title(f"Rotated {angle}°")
    plt.axis("off")

plt.tight_layout()
plt.show()