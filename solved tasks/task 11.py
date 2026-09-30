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

    # Make a copy of the original image
    noisy = image.copy()

    # Get image height and width
    height, width = image.shape[:2]

    # Total number of noisy pixels
    num_pixels = int(density * height * width)

    # Half salt and half pepper
    num_salt = num_pixels // 2
    num_pepper = num_pixels - num_salt

    # Random coordinates for salt noise
    y_salt = np.random.randint(0, height, num_salt)
    x_salt = np.random.randint(0, width, num_salt)

    # Set salt pixels to white
    noisy[y_salt, x_salt] = 255

    # Random coordinates for pepper noise
    y_pepper = np.random.randint(0, height, num_pepper)
    x_pepper = np.random.randint(0, width, num_pepper)

    # Set pepper pixels to black
    noisy[y_pepper, x_pepper] = 0

    return noisy


# Apply noise with density = 0.05
noisy_img = add_salt_pepper_noise(img, density=0.05)


# Display original and noisy images
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(cv.cvtColor(noisy_img, cv.COLOR_BGR2RGB))
plt.title("Salt & Pepper Noise (Density = 0.05)")
plt.axis("off")

plt.tight_layout()
plt.show()