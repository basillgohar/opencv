import cv2
import os
cap = cv2.VideoCapture(0)
datasets = 'dataset'
sub_data = 'basil'
path = os.path.join(datasets,sub_data)
if not os.path.isdir(path):
    os.mkdir(path)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haracades_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml') 

count = 1 

while count<3:
    _,frame = cap.read()
    original_frame= frame.copy()
    gray = cv2.cvtcolor(frame,cv2.BGR2GRAY)

    face=face_cascade.detectMultiScale(gray,1.3,5)#detectig face
    for x,y,w,h in face:
        cv2.rectange(frame,(x,y),(x+w,y+h),(0,255,255),2)

        face_roi = frame[y:y+h,x:x+w]
        gray_roi = gray[y:y+h,x:x+w]
        smile = smile_cascade.detectMultiScale(gray_roi,1.3,25)#detecting smile

        for x1,y1,w1,h1 in smile:
            cv2.rectange(face_roi,(x1,y1),(x1+w1,y1+h1),(255,255,0),2)#drawing rectangle around the smile
            cv2.imwrite(f'{path}/{count}',original_frame)#saving selfie
            print('selfie claimed')
            count = count+1

            if count>3:
                break
    cv2.imshow('camera star',frame)
    if cv2.waitKey(10) == ord(q): 
        break
