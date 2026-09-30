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

# Scale up by 1.2 using INTER_LINEAR
up_linear = cv.resize(
    img, None, fx=1.2, fy=1.2,
    interpolation=cv.INTER_LINEAR
)

# Scale up by 1.2 using INTER_NEAREST
up_nearest = cv.resize(
    img, None, fx=1.2, fy=1.2,
    interpolation=cv.INTER_NEAREST
)

# Scale down by 0.6 using INTER_LINEAR
down_linear = cv.resize(
    img, None, fx=0.6, fy=0.6,
    interpolation=cv.INTER_LINEAR
)

# Scale down by 0.6 using INTER_NEAREST
down_nearest = cv.resize(
    img, None, fx=0.6, fy=0.6,
    interpolation=cv.INTER_NEAREST
)

# Print shapes
print("Original shape:", img.shape)
print("Upscaled 1.2 shape:", up_linear.shape)
print("Downscaled 0.6 shape:", down_linear.shape)

# Display results
plt.figure(figsize=(15, 10))

plt.subplot(2, 3, 1)
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.title("Original")
plt.axis("off")

plt.subplot(2, 3, 2)
plt.imshow(cv.cvtColor(up_linear, cv.COLOR_BGR2RGB))
plt.title("Up 1.2 - INTER_LINEAR")
plt.axis("off")

plt.subplot(2, 3, 3)
plt.imshow(cv.cvtColor(up_nearest, cv.COLOR_BGR2RGB))
plt.title("Up 1.2 - INTER_NEAREST")
plt.axis("off")

plt.subplot(2, 3, 5)
plt.imshow(cv.cvtColor(down_linear, cv.COLOR_BGR2RGB))
plt.title("Down 0.6 - INTER_LINEAR")
plt.axis("off")

plt.subplot(2, 3, 6)
plt.imshow(cv.cvtColor(down_nearest, cv.COLOR_BGR2RGB))
plt.title("Down 0.6 - INTER_NEAREST")
plt.axis("off")

plt.tight_layout()
plt.show()