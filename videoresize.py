import cv2
#function declaration 
def rescaleFrame(frame,scale = 0.50):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[1]*scale)
    dimensions = (width,height)
    return cv2.resize(frame,dimensions)

#reading video 
capture = cv2.VideoCapture('OpenCV\dog.mp4')
while True:
    isTrue,frame = capture.read()
    frame_resized = rescaleFrame(frame,scale = 0.50)
    cv2.imshow('original video',frame)
    #rezie the loop
    cv2.imshow("resized video",frame_resized)
    #press q to close the outscreen 
    if cv2.waitKey(45) & 0XFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()