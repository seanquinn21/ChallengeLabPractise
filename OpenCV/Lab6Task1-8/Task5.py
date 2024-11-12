#Use the Raspberry Pi camera to capture a video and save it as task5.mp4. Use q to end
#the recording.

import cv2
from picamera2 import Picamera2
import time

# Initialize the camera
picam2 = Picamera2()

# Configure the camera to capture video at 640x480 resolution
config = picam2.create_video_configuration(main={"size": (640, 480)})
picam2.configure(config)

# Start the camera with a small delay to allow it to initialize
picam2.start()
time.sleep(2)  # Waits for 2 seconds

# Set up video writer with MP4 codec to save the video file
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('/home/pi/ee347/lab-6-python-and-opencv-2-group-17/task5.mp4', fourcc, 30, (640, 480))

print("Press 'q' to stop recording...")

# Main loop for capturing and saving video frames
while True:
    # Capture a frame from the camera
    frame = picam2.capture_array()

    # Convert the frame from RGB to BGR format (required for OpenCV compatibility)
    frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Write the frame to the output video file
    out.write(frame_bgr)

    # Display the frame in an OpenCV window
    cv2.imshow('Camera Capture', frame)

    # Stop recording if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video writer and close all windows after recording stops
out.release()
cv2.destroyAllWindows()
picam2.stop()
