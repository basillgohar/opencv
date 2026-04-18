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

