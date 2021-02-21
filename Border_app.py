
""" border_app.py
    Credit: Rodrigo Sparrapan
    sparodrigo82@gmail.com
    based on https://github.com/fsoubelet/ColorFrame """

    
import cv2
import glob 

count = 1

path = "drop-in/*CR2.jpg" 
path = "drop-in/*.jpg" 
path = "drop-in/*.JPG" 
filenames = glob.glob(path)

for filename in filenames:
        
        image = cv2.imread(filename)
        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        #image = cv2.resize(image, (6000, 40000))
        #image = cv2.imread(image)
        #gray_img = cv2.resize(gray_img, (6000, 4000))
    
        cv2.imwrite("drop-out/rebels_gray_" +str(count) +".jpg", gray_img)
        cv2.imwrite("drop-out/rebels_color_" +str(count) +".jpg", image)
    
        count += 1


from colorframe import BorderCreator


border_api = BorderCreator(commandline_path="drop-out/", vertical_border=30, horizontal_border=30, color="white")
border_api.execute_target()




