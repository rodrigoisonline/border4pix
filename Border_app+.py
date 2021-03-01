
""" border_app.py
    Credit: Rodrigo Sparrapan
    sparodrigo82@gmail.com
    based on https://github.com/fsoubelet/ColorFrame """

    
import cv2
import glob 

count = 1

path = "s_Top-10/Top_10_a_Olho/*.jpg" 
filenames = glob.glob(path)

for filename in filenames:
        
        image = cv2.imread(filename)
        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        #image = cv2.resize(image, (6000, 40000))
        #image = cv2.imread(image)
        #gray_img = cv2.resize(gray_img, (6000, 4000))
    
        
        cv2.imwrite("drop-out/a__rebels_color_" +str(count) +".jpg", image)
        cv2.imwrite("drop-out/z__rebels_gray_" +str(count) +".jpg", gray_img)
    
        count += 1


count = 1

path = "s_Top-10/Top_10_Entrada/*.jpg" 
filenames = glob.glob(path)

for filename in filenames:
        
        image = cv2.imread(filename)
        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        #image = cv2.resize(image, (6000, 40000))
        #image = cv2.imread(image)
        #gray_img = cv2.resize(gray_img, (6000, 4000))
    
        cv2.imwrite("drop-out/b__rebels_color_" +str(count) +".jpg", image)
        cv2.imwrite("drop-out/z__rebels_gray_" +str(count) +".jpg", gray_img)
    
        count += 1

count = 1

path = "s_Top-10/Top_10_Fila da Entrada/*.jpg" 
filenames = glob.glob(path)

for filename in filenames:
        
        image = cv2.imread(filename)
        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        #image = cv2.resize(image, (6000, 40000))
        #image = cv2.imread(image)
        #gray_img = cv2.resize(gray_img, (6000, 4000))
    
        cv2.imwrite("drop-out/c__rebels_color_" +str(count) +".jpg", image)
        cv2.imwrite("drop-out/z__rebels_gray_" +str(count) +".jpg", gray_img)
    
        count += 1

count = 1

path = "s_Top-10/Top_10_iPorta malas/*.jpg" 
filenames = glob.glob(path)

for filename in filenames:
        
        image = cv2.imread(filename)
        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        #image = cv2.resize(image, (6000, 40000))
        #image = cv2.imread(image)
        #gray_img = cv2.resize(gray_img, (6000, 4000))
    
        cv2.imwrite("drop-out/d__rebels_color_" +str(count) +".jpg", image)
        cv2.imwrite("drop-out/z__rebels_gray_" +str(count) +".jpg", gray_img)
    
        count += 1

count = 1

path = "s_Top-10/Top_10_Sem Carro/*.jpg" 
filenames = glob.glob(path)

for filename in filenames:
        
        image = cv2.imread(filename)
        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        #image = cv2.resize(image, (6000, 40000))
        #image = cv2.imread(image)
        #gray_img = cv2.resize(gray_img, (6000, 4000))
    
        cv2.imwrite("drop-out/e__rebels_color_" +str(count) +".jpg", image)
        cv2.imwrite("drop-out/z__rebels_gray_" +str(count) +".jpg", gray_img)
    
        count += 1


count = 1

path = "s_Top-10/Top_10_Transito da Entrada/*.jpg" 
filenames = glob.glob(path)

for filename in filenames:
        
        image = cv2.imread(filename)
        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        #image = cv2.resize(image, (6000, 40000))
        #image = cv2.imread(image)
        #gray_img = cv2.resize(gray_img, (6000, 4000))
    
        cv2.imwrite("drop-out/f__rebels_color_" +str(count) +".jpg", image)
        cv2.imwrite("drop-out/z__rebels_gray_" +str(count) +".jpg", gray_img)
    
        count += 1




count = 1

path = "s_Top-10/Top_10_Vol Criancas/*.jpg" 
filenames = glob.glob(path)

for filename in filenames:
        
        image = cv2.imread(filename)
        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        #image = cv2.resize(image, (6000, 40000))
        #image = cv2.imread(image)
        #gray_img = cv2.resize(gray_img, (6000, 4000))
    
        cv2.imwrite("drop-out/g__rebels_color_" +str(count) +".jpg", image)
        cv2.imwrite("drop-out/z__rebels_gray_" +str(count) +".jpg", gray_img)
    
        count += 1

count = 1

path = "s_Top-10/Top_10_Vol Trabalhando/*.jpg" 
filenames = glob.glob(path)

for filename in filenames:
        
        image = cv2.imread(filename)
        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        #image = cv2.resize(image, (6000, 40000))
        #image = cv2.imread(image)
        #gray_img = cv2.resize(gray_img, (6000, 4000))
    
        cv2.imwrite("drop-out/h__rebels_color_" +str(count) +".jpg", image)
        cv2.imwrite("drop-out/z__rebels_gray_" +str(count) +".jpg", gray_img)
    
        count += 1



path = "s_Top-10/Top_10_xFood/*.jpg" 
filenames = glob.glob(path)

for filename in filenames:
        
        image = cv2.imread(filename)
        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        #image = cv2.resize(image, (6000, 40000))
        #image = cv2.imread(image)
        #gray_img = cv2.resize(gray_img, (6000, 4000))
    
        cv2.imwrite("drop-out/i__rebels_color_" +str(count) +".jpg", image)
        cv2.imwrite("drop-out/z__rebels_gray_" +str(count) +".jpg", gray_img)
    
        count += 1




count = 1

path = "s_Top-10/Top_10_xRetrovisores/*.jpg" 
filenames = glob.glob(path)

for filename in filenames:
        
        image = cv2.imread(filename)
        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        #image = cv2.resize(image, (6000, 40000))
        #image = cv2.imread(image)
        #gray_img = cv2.resize(gray_img, (6000, 4000))
    
        cv2.imwrite("drop-out/j__rebels_color_" +str(count) +".jpg", image)
        cv2.imwrite("drop-out/z__rebels_gray_" +str(count) +".jpg", gray_img)
    
        count += 1

count = 1

path = "s_Top-10/Top_10_zEvangelistas/*.jpg" 
filenames = glob.glob(path)

for filename in filenames:
        
        image = cv2.imread(filename)
        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        #image = cv2.resize(image, (6000, 40000))
        #image = cv2.imread(image)
        #gray_img = cv2.resize(gray_img, (6000, 4000))
    
        cv2.imwrite("drop-out/k__rebels_color_" +str(count) +".jpg", image)
        cv2.imwrite("drop-out/z__rebels_gray_" +str(count) +".jpg", gray_img)
    
        count += 1


ount = 1

path = "s_Top-10/Top_10_zOracoes/*.jpg" 
filenames = glob.glob(path)

for filename in filenames:
        
        image = cv2.imread(filename)
        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        #image = cv2.resize(image, (6000, 40000))
        #image = cv2.imread(image)
        #gray_img = cv2.resize(gray_img, (6000, 4000))
    
        cv2.imwrite("drop-out/l__rebels_color_" +str(count) +".jpg", image)
        cv2.imwrite("drop-out/z__rebels_gray_" +str(count) +".jpg", gray_img)
    
        count += 1


from colorframe import BorderCreator


border_api = BorderCreator(commandline_path="drop-out/", vertical_border=33, horizontal_border=33, color="white")
border_api.execute_target()




