import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import sys


# Load image
path = r"C:\Users\ASUS\OneDrive\Desktop\skyexperts tasks\task 1\beautiful-natural-image-1844362_1280.jpg"

img = cv.imread(path, cv.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Could not read the image.")
    sys.exit()


# Custom Bilateral Filter
def custom_bilateral_filter(image, diameter, sigma_color, sigma_space):

    radius = diameter // 2

    # Padding around the image
    padded = cv.copyMakeBorder(
        image,
        radius,
        radius,
        radius,
        radius,
        cv.BORDER_REFLECT
    )

    # Output image
    output = np.zeros_like(image, dtype=np.float64)

    height, width = image.shape

    # Process each pixel
    for i in range(height):
        for j in range(width):

            center_pixel = float(image[i, j])

            weighted_sum = 0.0
            weight_total = 0.0

            for y in range(-radius, radius + 1):
                for x in range(-radius, radius + 1):

                    neighbor = float(
                        padded[i + radius + y,
                               j + radius + x]
                    )

                    # Spatial Gaussian weight
                    spatial_weight = np.exp(
                        -(x**2 + y**2) /
                        (2 * sigma_space**2)
                    )

                    # Intensity Gaussian weight
                    intensity_difference = neighbor - center_pixel

                    intensity_weight = np.exp(
                        -(intensity_difference**2) /
                        (2 * sigma_color**2)
                    )

                    # Combined bilateral weight
                    weight = spatial_weight * intensity_weight

                    weighted_sum += weight * neighbor
                    weight_total += weight

            output[i, j] = weighted_sum / weight_total

    return np.clip(output, 0, 255).astype(np.uint8)


# Parameters
diameter = 5
sigma_color = 50
sigma_space = 50


# Apply custom bilateral filter
custom_result = custom_bilateral_filter(
    img,
    diameter,
    sigma_color,
    sigma_space
)


# Apply OpenCV bilateral filter
opencv_result = cv.bilateralFilter(
    img,
    diameter,
    sigma_color,
    sigma_space
)


# Display results
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(img, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(custom_result, cmap="gray")
plt.title("Custom Bilateral Filter")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(opencv_result, cmap="gray")
plt.title("OpenCV Bilateral Filter")
plt.axis("off")

plt.tight_layout()
plt.show()