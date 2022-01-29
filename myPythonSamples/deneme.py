from os import read
import cv2
import time
import datetime
cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_fullbody.xml")

recording=True

frame_size = (int(cap.get(3)), int(cap.get(4)))
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("video.mp4", fourcc, 20, frame_size)

while True:
    _, frame = cap.read();

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3,5)
    bodies = face_cascade.detectMultiScale(gray, 1.3,5)

    if len(faces) + len(bodies) > 0:
        recording=True
    
    out.write(frame)

    #for(x, y, width, height) in faces:
    #    cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)

    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) == ord('q'):
        break
out.release()
cap.release()
cv2.destroyAllWindows()