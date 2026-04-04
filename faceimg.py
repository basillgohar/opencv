import cv2
import sys, numpy, os

haar_file = 'OpenCV\haar_face.xml'
datasets = 'dataset'

sub_data = 'basil'

path = os.path.join(datasets,sub_data)

if not os.path.isdir(path):
    os.mkdir(path)

(width,height) = (130,200)

face_cascade = cv2.CascadeClassifier(haar_file)
webcam = cv2.VideoCapture(0)
print("[INFO] Capturing face images.Press 'q' to quit" )

count = 1
while count < 10:
    _, frame = webcam.read()
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_img,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        face = gray_img[y:y + h, x:x + w]#extracting face form img
        face_resize = cv2.resize(face,(width,height))#resizeing the face 
        cv2.imwrite(f'{path}/{count}.png',face_resize)
        count+=1

        if count >10:
            break
    cv2.imshow('Face Capture',frame)
    if cv2.waitKey(10) == ord('q'):
        break
print('[INFO]Capture complete/exiting...')
webcam.release()
cv2.destroyAllWindows()

