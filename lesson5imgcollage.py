import cv2 
import os
from PIL import Image

os.chdir(r"OpenCV\lesson5img")
path = r"OpenCV\lesson5img"
mean_height = 0
mean_width = 0 

num_of_images= len(os.listdir("."))
#resizeing all images to mian width and height 
for file in os.listdir('.'):
    
    img = Image.open(os.path.join(path,file))
    width,height = img.size
    mean_width = mean_width+width
    mean_height = mean_height+height

    print(mean_width)
    print(mean_height)

    for file in os.listdir('.'):
        if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
            img = Image.open(os.path.join(path, file))
            width, height = img.size
            print(width, height)

            imgResized = img.resize((mean_width,mean_height),Image.LANCZOS)
            print(img.filename.split('\\'[-1]), "is resized")





def videoGenerator():
    video_name = "MyFristVideo.avi"
    os.chdir(r"OpenCV\lesson5img")