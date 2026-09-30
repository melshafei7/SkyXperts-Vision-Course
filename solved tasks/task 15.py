import cv2 as cv
import numpy as np
import sys


# Function to add salt and pepper noise
def add_salt_pepper_noise(image, density=0.05):

    noisy = image.copy()
    height, width = image.shape

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


# Camera settings
camera_id = 0

cap = cv.VideoCapture(camera_id)

# Check if camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    sys.exit()


# Sharpening kernel
sharpen_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])


while cap.isOpened():

    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    # Stage 1: Original camera frame
    original = frame

    # Stage 2: Convert to grayscale
    gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)

    # Stage 3: Add salt and pepper noise
    noisy = add_salt_pepper_noise(gray, density=0.05)

    # Stage 4: Remove noise using median filter
    median = cv.medianBlur(noisy, 5)

    # Stage 5: Sharpen the filtered image
    sharpened = cv.filter2D(
        median,
        -1,
        sharpen_kernel
    )

    # Display all stages in separate windows
    cv.imshow("1 - Original Camera", original)
    cv.imshow("2 - Grayscale", gray)
    cv.imshow("3 - Salt and Pepper Noise", noisy)
    cv.imshow("4 - Median Filter", median)
    cv.imshow("5 - Sharpened", sharpened)

    # Press q to quit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break


# Release camera and close all windows
cap.release()
cv.destroyAllWindows()