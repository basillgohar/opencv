import cv2 
import numpy as np
import time

raw_video = cv2.videoCapture('OpenCV\lesson5img\MyFristVideo.avi')
time.sleep(1)

count = 0
background = 0

for i in range(60):
    return_val,background = raw_video.read()
    
    if return_val == False:
        continue

background = np.flip(background, axis = 1)

while(raw_video.isOpened()):
    return_val, img =raw_video.read()
    if not return_val: 
        break
    count = count + 1
    img = np.flip(img, axix = 1)
    hsv = cv2.cvtColot(img, cv2.COLOR_BGR2HSV) 
    
    lower_red1 = np.array([100,40,40])
    upper_red1 = np.array([100,255,255])

    lower_red2 = np.array([155,40,40])
    upper_red2 = np.array([180,255,255])

    mask1 = cv2.inrange(hsv, lower_red1,upper_red1)
    mask2 = cv2.inrange(hsv, lower_red2,upper_red2)

    mask1 = mask1 + mask2

    red_mask = cv2.bitwise_or(mask1, mask2)
    
