#------------------------------------------------#
#   1. Basic Image Manipulation
#------------------------------------------------#
# Load an image, resize it to a specified dimension, and rotate it by 90 degrees.
# This demonstrates how to load an image, change its size, and apply a rotation.
# Useful functions: cv2.resize() and cv2.rotate()

import cv2

# Load the image
image = cv2.imread("input.jpg")

# Resize the image to 300x300 pixels
resized_image = cv2.resize(image, (300, 300))

# Rotate the image 90 degrees clockwise
rotated_image = cv2.rotate(resized_image, cv2.ROTATE_90_CLOCKWISE)

# Save the output image
cv2.imwrite("output.jpg", rotated_image)

#------------------------------------------------#
#   2. Filtering and Image Blurring
#------------------------------------------------#
# Apply a Gaussian blur and a median blur to an image and display both results side-by-side.
# This is commonly used for noise reduction and smoothing. 
# Useful functions: cv2.GaussianBlur() and cv2.medianBlur()

import cv2
import numpy as np

# Load the image
image = cv2.imread("input.jpg")

# Apply Gaussian blur
gaussian_blur = cv2.GaussianBlur(image, (15, 15), 0)

# Apply Median blur
median_blur = cv2.medianBlur(image, 15)

# Stack and display the blurred images side by side
combined = np.hstack((gaussian_blur, median_blur))
cv2.imshow("Gaussian vs Median Blur", combined)
cv2.waitKey(0)
cv2.destroyAllWindows()


#------------------------------------------------#
#   3. Edge Detection with Canny Edge Detector
#------------------------------------------------#
# Use the Canny edge detector to find edges in an image.
# Edge detection highlights areas of high contrast in the image.
# Useful function: cv2.Canny()

import cv2

# Load the image in grayscale
image = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

# Apply Canny edge detection
edges = cv2.Canny(image, 100, 200)

# Display the edges
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()


#------------------------------------------------#
#   4. Color Space Conversion
#------------------------------------------------#
# Convert an image from BGR to HSV color space and isolate a specific color range (e.g., blue).
# This technique is useful for color-based segmentation.
# Useful functions: cv2.cvtColor(), cv2.inRange(), cv2.bitwise_and()

import cv2
import numpy as np

# Load the image
image = cv2.imread("input.jpg")

# Convert BGR image to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the HSV range for the color blue
lower_blue = np.array([100, 150, 0])
upper_blue = np.array([140, 255, 255])

# Create a mask to isolate blue regions
mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

# Apply the mask to the original image
result = cv2.bitwise_and(image, image, mask=mask)

# Display the isolated blue areas
cv2.imshow("Blue Color Isolation", result)
cv2.waitKey(0)
cv2.destroyAllWindows()


#------------------------------------------------#
#   5. Drawing on Images
#------------------------------------------------#
# Draw shapes (circle, rectangle, and line) on an image and label each shape with text.
# Useful for adding annotations or highlighting areas of interest.
# Useful functions: cv2.circle(), cv2.rectangle(), cv2.line(), cv2.putText()

import cv2

# Load the image
image = cv2.imread("input.jpg")

# Draw a blue filled circle
cv2.circle(image, (150, 150), 50, (255, 0, 0), -1)

# Draw a green rectangle
cv2.rectangle(image, (200, 50), (300, 150), (0, 255, 0), 3)

# Draw a red line
cv2.line(image, (100, 200), (300, 200), (0, 0, 255), 5)

# Add text labels for each shape
cv2.putText(image, "Circle", (130, 140), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
cv2.putText(image, "Rectangle", (200, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
cv2.putText(image, "Line", (100, 220), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

# Display the image with shapes
cv2.imshow("Shapes", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


#------------------------------------------------#
#   6. Video Processing and Frame Manipulation
#------------------------------------------------#
# Read frames from a video file, apply grayscale filter, and display frames in real-time.
# Useful for frame-by-frame video processing.
# Useful functions: cv2.VideoCapture(), cv2.cvtColor()

import cv2

# Open the video file
cap = cv2.VideoCapture("video.mp4")

# Process each frame in the video
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the grayscale frame
    cv2.imshow("Grayscale Video", gray_frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object
cap.release()
cv2.destroyAllWindows()


#------------------------------------------------#
#   7. Face Detection in Live Video Feed
#------------------------------------------------#
# Use a webcam feed to detect faces in real-time and draw bounding boxes around each face.
# Useful for applications like face recognition and security.
# Useful functions: cv2.CascadeClassifier(), detectMultiScale()

import cv2

# Load the face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Capture video from webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frame with detected faces
    cv2.imshow("Face Detection", frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture
cap.release()
cv2.destroyAllWindows()


#------------------------------------------------#
#   8. Template Matching
#------------------------------------------------#
# Use template matching to locate a smaller template image within a larger main image.
# Useful for finding specific patterns or objects in images.
# Useful functions: cv2.matchTemplate(), cv2.minMaxLoc()

import cv2

# Load the main image and the template
main_image = cv2.imread("main_image.jpg")
template = cv2.imread("template.jpg", cv2.IMREAD_GRAYSCALE)
main_gray = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)

# Perform template matching
result = cv2.matchTemplate(main_gray, template, cv2.TM_CCOEFF_NORMED)
_, _, _, max_loc = cv2.minMaxLoc(result)

# Get coordinates of the bounding box
top_left = max_loc
h, w = template.shape
bottom_right = (top_left[0] + w, top_left[1] + h)

# Draw a rectangle around the matched area
cv2.rectangle(main_image, top_left, bottom_right, (0, 255, 0), 2)

# Display the result
cv2.imshow("Template Match", main_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


