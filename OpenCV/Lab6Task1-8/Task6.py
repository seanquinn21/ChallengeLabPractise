#Copy the code from task 5 and save the video as a numpy file. Ensure the storage space
#used is minimised without loss of data.

import cv2
from picamera2 import Picamera2, Preview
import numpy as np
import time

# Initialize the camera
picam2 = Picamera2()

# Configure the camera to preview at 640x480 resolution
camera_config = picam2.create_preview_configuration(main={"size": (640, 480)})
picam2.configure(camera_config)

# Start the camera and wait a moment to ensure it's fully initialized
picam2.start()
time.sleep(2)  # Delay to allow the camera to adjust

# Set frame dimensions
frame_width = 640
frame_height = 480

# Initialize an empty list to store captured frames
frames = []

# Capture loop
while True:
    # Capture a frame from the camera
    frame = picam2.capture_array()

    # Rotate the frame 180 degrees
    frame = cv2.rotate(frame, cv2.ROTATE_180)

    # Convert the frame from RGB to BGR format for OpenCV compatibility
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Append the processed frame to the list of frames
    frames.append(frame)

    # Display the frame in an OpenCV window
    cv2.imshow("Task 6", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

# Convert the list of frames to a numpy array for saving
frames_array = np.array(frames, dtype=np.uint8)

# Save the frames array to a file in .npy format
np.save("task6.npy", frames_array)

# Stop the camera and close all OpenCV windows
picam2.stop()
cv2.destroyAllWindows()

