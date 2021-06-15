import cv2
face_cascade = cv2.CascadeClassifier('/home/aayush/Downloads/haarcascade_frontalface_default.xml')


VideoCapture = cv2.VideoCapture('/home/aayush/Desktop/ARK_Task_2/WIN_20210531_22_01_21_Pro.mp4')

def rescaleFrame(frame, scale = 0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

def detect(gray, frame_new):
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame_new, (x, y), (x+w, y+h), (255, 0, 0), 2)
    return frame_new

while (VideoCapture.isOpened()):
    _, frame = VideoCapture.read()
    frame_new = rescaleFrame(frame)
    gray = cv2.cvtColor(frame_new, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame_new)
    cv2.imshow('frame', canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


VideoCapture.release()
cv2.destroyAllWindows()