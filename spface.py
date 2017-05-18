import cv2
import sys
import time

# haarcascade_frontalface_alt was taken from the OpenCV project 2.4.9 TAG
# https://github.com/opencv/opencv/tree/2.4.9

cascPath = 'haarcascade_frontalface_alt.xml'
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)
video_capture.set(3,1280)
video_capture.set(4,720)

while True:
    # time.sleep(2)
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # Cut the faces into separate files with timestamp
    for (x, y, w, h) in faces:
        # Draw rectangle around the faces
        cv2.rectangle(frame, (x-50, y-50), (x+w+50, y+h+50),(0,255,0),0)
        head = frame[y-50:y+h+50, x-50:x+w+50]
        filename="head{}".format(int(time.time()))
        # cv2.imshow(filename, head)
        cv2.imwrite(filename+".png", head)
        time.sleep(1)

    # Display the resulting frame
    # cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
