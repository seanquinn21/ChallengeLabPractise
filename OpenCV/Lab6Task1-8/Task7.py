#Load task1.mp4 and use haarcascades to detect all faces in the video. Draw a bounding
#box around the faces and display the output in a preview window

import cv2

# Load the Haar Cascade for face detection
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Specify the input video file
inputVid = "task1.mp4"

# Open the video file
cap = cv2.VideoCapture(inputVid)

# Get the video frame width, height, and frames per second (fps)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Process each frame in the video
while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Break the loop if there are no more frames (end of video)
    if not ret:
        print("End of video")
        break

    # Convert the frame to grayscale (required for face detection)
    greyFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = faceCascade.detectMultiScale(
        greyFrame,
        scaleFactor=1.05,      # Parameter for adjusting scale to detect faces of different sizes
        minNeighbors=5,        # Minimum number of neighbors for each rectangle to be considered a face
        minSize=(60, 60)       # Minimum size of the face to detect
    )

    # Draw a green rectangle around each detected face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the frame with detected faces
    cv2.imshow("Task 9", frame)

    # Exit if the 'q' key is pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
