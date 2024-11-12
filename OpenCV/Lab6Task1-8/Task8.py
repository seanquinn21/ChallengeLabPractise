
#Using the Raspberry Pi Camera, capture frames and use haarcascades to detect one
#face in the frame. Display the frame with the bounding box, and in a separate window,
#display the cropped face


import cv2
from picamera2 import Picamera2

# Initialize the camera
picam2 = Picamera2()

# Configure the camera preview to 640x480 resolution with the XRGB8888 format
camera_config = picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)})
picam2.configure(camera_config)
picam2.start()

# Load the Haar Cascade model for face detection
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Main loop to capture frames and detect faces
while True:
    # Capture a frame from the camera
    frame = picam2.capture_array()

    # Rotate the frame 180 degrees
    frame = cv2.rotate(frame, cv2.ROTATE_180)

    # Convert the frame to grayscale for face detection
    greyFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = faceCascade.detectMultiScale(
        greyFrame,
        scaleFactor=1.05,        # Scale factor to adjust face detection sensitivity
        minNeighbors=5,          # Minimum neighbors needed for a rectangle to qualify as a face
        minSize=(100, 100)       # Minimum size of faces to detect
    )

    # Draw rectangles around each detected face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # If any faces are detected, crop and display the first detected face
    if len(faces) > 0:
        # Coordinates of the first detected face
        (x, y, w, h) = faces[0]

        # Draw a green rectangle around the first detected face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Crop the region of the detected face from the frame
        face_crop = frame[y:y + h, x:x + w]

        # Display the cropped face in a separate window
        cv2.imshow('Face', face_crop)

    # Display the main frame with face detection in a window named "Task 8"
    cv2.imshow("Task 8", frame)

    # Exit the loop if 'q' key is pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Cleanup: Stop the camera and close all OpenCV windows
picam2.stop()
cv2.destroyAllWindows()
