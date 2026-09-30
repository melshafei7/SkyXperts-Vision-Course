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

# ------------------------------------------------
# Method 1: Rotate 45 degrees and scale by 0.5
# in ONE operation
# ------------------------------------------------

center = (width // 2, height // 2)

rotation_matrix = cv.getRotationMatrix2D(
    center,
    45,
    0.5
)

rotate_scale = cv.warpAffine(
    img,
    rotation_matrix,
    (width, height)
)

# ------------------------------------------------
# Method 2: Resize first, then rotate
# ------------------------------------------------

# Resize to 50%
resized = cv.resize(
    img,
    None,
    fx=0.5,
    fy=0.5,
    interpolation=cv.INTER_LINEAR
)

# Get dimensions of resized image
h2, w2 = resized.shape[:2]
center2 = (w2 // 2, h2 // 2)

# Rotation matrix (no additional scaling)
rotation_matrix2 = cv.getRotationMatrix2D(
    center2,
    45,
    1.0
)

separate = cv.warpAffine(
    resized,
    rotation_matrix2,
    (w2, h2)
)

# ------------------------------------------------
# Display results
# ------------------------------------------------

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.title("Original")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(cv.cvtColor(rotate_scale, cv.COLOR_BGR2RGB))
plt.title("Rotate 45° + Scale 0.5\nOne Operation")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(cv.cvtColor(separate, cv.COLOR_BGR2RGB))
plt.title("Resize 0.5 then Rotate 45°")
plt.axis("off")

plt.tight_layout()
plt.show()

# Compare shapes
print("Original shape:", img.shape)
print("One operation shape:", rotate_scale.shape)
print("Separate operations shape:", separate.shape)