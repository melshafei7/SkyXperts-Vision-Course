import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import sys

# Load image
path = r"C:\Users\ASUS\OneDrive\Desktop\skyexperts tasks\task 1\images.jpg"

img = cv.imread(path, cv.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Could not read the image.")
    sys.exit()


# Function to add salt and pepper noise
def add_salt_pepper_noise(image, density=0.05):

    noisy = image.copy()
    height, width = image.shape

    num_pixels = int(density * height * width)

    num_salt = num_pixels // 2
    num_pepper = num_pixels - num_salt

    # Salt
    y = np.random.randint(0, height, num_salt)
    x = np.random.randint(0, width, num_salt)
    noisy[y, x] = 255

    # Pepper
    y = np.random.randint(0, height, num_pepper)
    x = np.random.randint(0, width, num_pepper)
    noisy[y, x] = 0

    return noisy


# Adaptive Median Filter
def adaptive_median_filter(image, max_size=7):

    output = image.copy()

    max_pad = max_size // 2
    padded = cv.copyMakeBorder(
        image,
        max_pad,
        max_pad,
        max_pad,
        max_pad,
        cv.BORDER_REFLECT
    )

    height, width = image.shape

    for i in range(height):
        for j in range(width):

            window_size = 3

            while window_size <= max_size:

                half = window_size // 2

                center_y = i + max_pad
                center_x = j + max_pad

                window = padded[
                    center_y-half:center_y+half+1,
                    center_x-half:center_x+half+1
                ]

                z_min = np.min(window)
                z_max = np.max(window)
                z_med = np.median(window)
                z_xy = image[i, j]

                # Stage A
                if z_min < z_med < z_max:

                    # Stage B
                    if z_min < z_xy < z_max:
                        output[i, j] = z_xy
                    else:
                        output[i, j] = z_med

                    break

                else:
                    window_size += 2

                    if window_size > max_size:
                        output[i, j] = z_med

    return output


# Add noise
noisy_img = add_salt_pepper_noise(img, density=0.05)

# Standard median filter
standard_median = cv.medianBlur(noisy_img, 5)

# Adaptive median filter
adaptive_median = adaptive_median_filter(noisy_img, max_size=7)


# Display results
plt.figure(figsize=(14, 10))

plt.subplot(2, 2, 1)
plt.imshow(img, cmap="gray")
plt.title("Original")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(noisy_img, cmap="gray")
plt.title("Salt & Pepper Noise")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(standard_median, cmap="gray")
plt.title("Standard Median 5x5")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(adaptive_median, cmap="gray")
plt.title("Adaptive Median (Max 7x7)")
plt.axis("off")

plt.tight_layout()
plt.show()