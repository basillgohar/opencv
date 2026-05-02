import cv2
#capturing frames form video
cap = cv2.VideoCapture('OpenCV/vehicle_detect\cars.mp4')

#trained XML classfiers descrobes some fetures of some obhect er eant to detect

car_cascade = cv2.CascadeClassifier('OpenCV/vehicle_detect\cars.xml')

#loop run if capturing has been intionlized
#reading frames from video
while True: 
    ret,frames = cap.read()
    #convert rgb into gray scale of each frame
    gray = cv2.cvtColor(frames,cv2.COLOR_BGR2GRAY)
    #detect cars of diffrent sizes in the video
    cars = car_cascade.detectMultiScale(gray,1.1,1)
    #to draw the rectangle for each car
    for (x,y,w,h) in cars:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(234,40,120),5)
    #display in the window
    cv2.imshow('detect vehicles',frames)
    #press esc key to stop the video
    if cv2.waitKey(33)==27:
        break
#de allocate any assocated memory
cv2.destroyAllWindows()
