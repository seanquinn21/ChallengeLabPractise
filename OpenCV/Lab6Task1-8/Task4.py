#Load task1.mp4, run Gaussian blur on the video and save as task4.mp4.

import cv2

video_path = 'task1.mp4'
output_path = 'task4.mp4'

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

while True:
    ret, frame = cap.read()
    if not ret:
        print("Reached the end of the video.")
        break

    blurred_frame = cv2.GaussianBlur(frame, (15, 15), 0)
    out.write(blurred_frame)

    
    cv2.imshow('Blurred Video', blurred_frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows() 