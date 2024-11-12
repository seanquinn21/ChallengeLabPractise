#Using the OpenCV draw functions (line, rectangle, circle), load task1.mp4 and draw a
#moving progress bar on the bottom of the video preview

import cv2

video_path = 'task1.mp4'
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    ret, frame = cap.read()
    if not ret:
        print("Reached the end of the video.")
        break

    current_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
    progress = int((current_frame / total_frames) * width)

    # Draw the progress bar at the bottom of the frame
    cv2.rectangle(frame, (0, height - 20), (progress, height - 5), (0, 255, 0), -1)

    cv2.imshow('Video with Progress Bar', frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()