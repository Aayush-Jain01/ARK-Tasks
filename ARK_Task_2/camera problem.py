import cv2

VideoCapture = cv2.VideoCapture(-1)

while True:
    _, frame = VideoCapture.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break