#Load task1.mp4 and display it in an OpenCV window.

import cv2

video_path = 'task1.mp4'
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Reached the end of the video.")
        break

    cv2.imshow('Video Playback', frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()