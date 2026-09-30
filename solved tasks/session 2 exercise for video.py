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

    # Salt
    y_salt = np.random.randint(0, height, num_salt)
    x_salt = np.random.randint(0, width, num_salt)
    noisy[y_salt, x_salt] = 255

    # Pepper
    y_pepper = np.random.randint(0, height, num_pepper)
    x_pepper = np.random.randint(0, width, num_pepper)
    noisy[y_pepper, x_pepper] = 0

    return noisy


# Sharpening kernel
sharpen_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])


# Video path
video_path = r"C:\Users\ASUS\OneDrive\Desktop\skyexperts tasks\exercise\input_video.mp4"

cap = cv.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    sys.exit()


while True:

    ret, frame = cap.read()

    if not ret:
        break

    # 1. Convert frame to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # 2. Sharpen frame
    sharpened = cv.filter2D(
        gray,
        -1,
        sharpen_kernel
    )

    # 3. Add salt and pepper noise
    noisy = add_salt_pepper_noise(
        sharpened,
        density=0.05
    )

    # 4. Remove salt and pepper noise
    filtered = cv.medianBlur(noisy, 5)

    # Display all stages
    cv.imshow("1 - Original Video", frame)
    cv.imshow("2 - Grayscale", gray)
    cv.imshow("3 - Sharpened", sharpened)
    cv.imshow("4 - Salt and Pepper Noise", noisy)
    cv.imshow("5 - Noise Removed", filtered)

    # Press q to quit
    if cv.waitKey(25) & 0xFF == ord('q'):
        break


cap.release()
cv.destroyAllWindows()import cv2 as cv
import numpy as np
import sys


# Function to add salt and pepper noise
def add_salt_pepper_noise(image, density=0.05):

    noisy = image.copy()
    height, width = image.shape

    num_pixels = int(density * height * width)
    num_salt = num_pixels // 2
    num_pepper = num_pixels - num_salt

    # Salt
    y_salt = np.random.randint(0, height, num_salt)
    x_salt = np.random.randint(0, width, num_salt)
    noisy[y_salt, x_salt] = 255

    # Pepper
    y_pepper = np.random.randint(0, height, num_pepper)
    x_pepper = np.random.randint(0, width, num_pepper)
    noisy[y_pepper, x_pepper] = 0

    return noisy


# Sharpening kernel
sharpen_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])


# Video path
video_path = r"C:\Users\ASUS\OneDrive\Desktop\skyexperts tasks\exercise\input_video.mp4"

cap = cv.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    sys.exit()


while True:

    ret, frame = cap.read()

    if not ret:
        break

    # 1. Convert frame to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # 2. Sharpen frame
    sharpened = cv.filter2D(
        gray,
        -1,
        sharpen_kernel
    )

    # 3. Add salt and pepper noise
    noisy = add_salt_pepper_noise(
        sharpened,
        density=0.05
    )

    # 4. Remove salt and pepper noise
    filtered = cv.medianBlur(noisy, 5)

    # Display all stages
    cv.imshow("1 - Original Video", frame)
    cv.imshow("2 - Grayscale", gray)
    cv.imshow("3 - Sharpened", sharpened)
    cv.imshow("4 - Salt and Pepper Noise", noisy)
    cv.imshow("5 - Noise Removed", filtered)

    # Press q to quit
    if cv.waitKey(25) & 0xFF == ord('q'):
        break


cap.release()
cv.destroyAllWindows()