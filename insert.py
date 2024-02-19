import pyautogui as pag
import mss, cv2
import numpy as np
import PIL
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#time_icon = {'left' : -565, 'top' : 163, 'width' : 30 ,'height' : 20}
#time_icon = {'left' : -1200, 'top' : 530, 'width' : 500 ,'height' : 50}
insert_icon = {'left' : -570, 'top' : 160, 'width' : 30 ,'height' : 30}
time_icon = {'left' : -1770, 'top' : 1010, 'width' : 100 ,'height' : 20}


while True :
    x,y = pag.position()
    position_str = 'X: ' +str(x) + 'Y: ' + str(y)
    with mss.mss() as sct :
        time_img = np.array(sct.grab(time_icon))[:,:,:]
        cv2.imshow('time_img',time_img)
        cv2.waitKey(0)
        result = pytesseract.image_to_string(time_img,config='--psm 6')
        result.remove(3)
        print(len(result))
        print(result[-5]) 