import cv2 
import os
from PIL import Image

#os.chdir(r"C:\Users\gohar\OneDrive\Desktop\JETLEARN\OpenCV\lesson5img")
#path = r"C:\Users\gohar\OneDrive\Desktop\JETLEARN\OpenCV\lesson5img"

os.chdir(r"C:\Users\gohar\OneDrive\Desktop\JETLEARN\OpenCV\lesson5img")
path = r"C:\Users\gohar\OneDrive\Desktop\JETLEARN\OpenCV\lesson5img"
mean_height = 0
mean_width = 0 

num_of_images= len(os.listdir("."))
#resizeing all images to mian width and height 
for file in os.listdir('.'):
    
    img = Image.open(os.path.join(path,file))
    width,height = img.size
    mean_width = mean_width + width
    mean_height = mean_height + height

    mean_height = mean_height // num_of_images
    mean_width = mean_width // num_of_images

    print(mean_width)
    print(mean_height)

    for file in os.listdir('.'):
        if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
            img = Image.open(os.path.join(path, file))
            width, height = img.size
            print(width, height)

            imgResized = img.resize((mean_width,mean_height),Image.LANCZOS)
            imgResized.save(file,'JPEG',quality = 95)
            print(img.filename.split('\\')[-1], "is resized")





def videoGenerator():
    video_name = "MyFristVideo.avi"
    os.chdir(r"OpenCV\lesson5img")
    images = []
    for img in os.lisdir('.'):
        if img.endswiyh('.jpg')or img.endswith('.jpeg') or img.endswith('.png'):
            images.append(img)

    print(images)

    frame = cv2.imread(os.path.join(".",images[0]))
    height,width,layer = frame.shape
    video = cv2.VideoWriter(video_name,0,1,(width,height))
    for image in images:
        video.write(cv2.imread(os.path.join(".",image)))  

    cv2.destroyAllWindows()
    video.release()
    print("video Generated")
videoGenerator()
