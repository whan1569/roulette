import pyautogui as pag
import mss, cv2
import numpy as np
import pytesseract
from PIL import Image
import time
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

time_icon = {'left' : -1200, 'top' : 530, 'width' : 500 ,'height' : 50}
insert_icon = {'left' : -565, 'top' : 163, 'width' : 30 ,'height' : 20}

low_button = [-2080 , 1080]
even_button = [-1880 , 1080]
red_button = [-1680 , 1080]
black_button = [-1480 , 1080]
odd_button = [-1280 , 1080]
high_button = [-1080 , 1080]
red = []
red [0:10] =[0,1,0,1,0,1,0,1,0,1,0]
red [11:20] = [0,1,0,1,0,1,0,1,1,0]
red [21:30] = [1,0,1,0,1,0,1,0,0,1]
red [31:36] = [0,1,0,1,0,1]
color_his = 3
even_his = 3
high_his = 3
def click(coords):
    pag.moveTo(x = coords[0], y = coords[1], duration = 0.0)
    pag.mouseDown()
    pag.mouseUp()
while True:
    x,y = pag.position()
    position_str = 'X: ' +str(x) + 'Y: ' + str(y)
    with mss.mss() as sct :
        time_img = np.array(sct.grab(time_icon))[:,:,:3]
        insert_img = np.array(sct.grab(insert_icon))[:,:,:3]
        result = pytesseract.image_to_string(time_img, lang = 'kor')
    if result =='베팅을 하십시오. 14\n' :
        with mss.mss() as sct :
            a = pytesseract.image_to_string(insert_img, config = '--psm 6')
        if a=='0)\n' : 
            a = b
        else :
            a = int(a)
            b = a 
        print(a)
        color_check = red[a]
        even_check = a%2
        if a<=18 :
            high_check = 0
        else:
            high_check = 1
        if color_check != color_his :
            color_his = color_check
            color_count = 0
        if even_check != even_his :
            even_his = even_check
            even_count = 0
        if high_check != high_his :
            high_his = high_check
            high_count = 0
        color_count= color_count + 1
        even_count = even_count + 1
        high_count = high_count + 1
        if high_count > 2  and high_count < 8:
            j = 1
            if high_check == 0 :
                for i in range(3,high_count):
                    j = j*2
                for i in range(0,j): 
                    click(high_button)
            elif high_check == 1 :
                for i in range(3,high_count):
                    j = j*2
                for i in range(0,j): 
                    click(low_button)
        
        if color_count > 2 and color_count < 8:
            j = 1
            if color_check == 0 :
                for i in range(3,color_count):
                    j = j*2
                for i in range(0,j): 
                    click(red_button)
            elif color_check == 1 :
                for i in range(3,color_count):
                    j = j*2
                for i in range(0,j): 
                    click(black_button)
        
        if even_count > 2 and even_count < 8:
            j = 1
            if even_check == 0 :
                for i in range(3,even_count):
                    j = j*2
                for i in range(0,j): 
                    click(odd_button)
            elif even_check == 1 :
                for i in range(3,even_count):
                    j = j*2
                for i in range(0,j):
                    click(even_button)
        time.sleep(1.5)     # 2초 기다림
    

    