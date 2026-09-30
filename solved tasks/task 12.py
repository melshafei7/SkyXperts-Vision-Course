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


# Function to add salt and pepper noise
def add_salt_pepper_noise(image, density=0.05):

    noisy = image.copy()

    height, width = image.shape[:2]

    num_pixels = int(density * height * width)

    num_salt = num_pixels // 2
    num_pepper = num_pixels - num_salt

    # Salt noise
    y_salt = np.random.randint(0, height, num_salt)
    x_salt = np.random.randint(0, width, num_salt)
    noisy[y_salt, x_salt] = 255

    # Pepper noise
    y_pepper = np.random.randint(0, height, num_pepper)
    x_pepper = np.random.randint(0, width, num_pepper)
    noisy[y_pepper, x_pepper] = 0

    return noisy


# Add salt and pepper noise
noisy_img = add_salt_pepper_noise(img, density=0.05)

# Apply median filters with different kernel sizes
median_3 = cv.medianBlur(noisy_img, 3)
median_5 = cv.medianBlur(noisy_img, 5)
median_7 = cv.medianBlur(noisy_img, 7)


# Display results
plt.figure(figsize=(15, 10))

plt.subplot(2, 3, 1)
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 3, 2)
plt.imshow(cv.cvtColor(noisy_img, cv.COLOR_BGR2RGB))
plt.title("Salt & Pepper Noise")
plt.axis("off")

plt.subplot(2, 3, 3)
plt.imshow(cv.cvtColor(median_3, cv.COLOR_BGR2RGB))
plt.title("Median Filter 3x3")
plt.axis("off")

plt.subplot(2, 3, 4)
plt.imshow(cv.cvtColor(median_5, cv.COLOR_BGR2RGB))
plt.title("Median Filter 5x5")
plt.axis("off")

plt.subplot(2, 3, 5)
plt.imshow(cv.cvtColor(median_7, cv.COLOR_BGR2RGB))
plt.title("Median Filter 7x7")
plt.axis("off")

plt.tight_layout()
plt.show()