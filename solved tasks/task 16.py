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


# Path of input video
video_path = r"C:\Users\ASUS\OneDrive\Desktop\skyexperts tasks\task 1\326081.mp4"

# Open video
cap = cv.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    sys.exit()


# Get video properties
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv.CAP_PROP_FPS)

print("Video size:", width, "x", height)
print("FPS:", fps)


# Output video settings
output_path = r"C:\Users\ASUS\OneDrive\Desktop\skyexperts tasks\task 16\processed_video.mp4"

fourcc = cv.VideoWriter_fourcc(*"mp4v")

out = cv.VideoWriter(
    output_path,
    fourcc,
    fps,
    (width, height),
    isColor=False
)

if not out.isOpened():
    print("Error: Could not create output video.")
    cap.release()
    sys.exit()


# Sharpening kernel
sharpen_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])


# Process video frame by frame
while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Stage 1: Convert to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Stage 2: Add salt and pepper noise
    noisy = add_salt_pepper_noise(gray, density=0.05)

    # Stage 3: Remove noise using median filter
    median = cv.medianBlur(noisy, 5)

    # Stage 4: Sharpen
    sharpened = cv.filter2D(
        median,
        -1,
        sharpen_kernel
    )

    # Save final processed frame
    out.write(sharpened)

    # Display stages
    cv.imshow("Original Video", frame)
    cv.imshow("Grayscale", gray)
    cv.imshow("Salt and Pepper Noise", noisy)
    cv.imshow("Median Filter", median)
    cv.imshow("Final Sharpened", sharpened)

    # Press q to stop
    if cv.waitKey(1) & 0xFF == ord("q"):
        break


# Release resources
cap.release()
out.release()
cv.destroyAllWindows()

print("Processing completed.")
print("Saved video:", output_path)