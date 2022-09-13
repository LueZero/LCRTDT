#coding=utf-8

import os
from traceback import print_tb
import numpy as np
import pytesseract
import operator
import cv2
import re
import platform

import pyautogui
import pyperclip
import keyboard,time

from time import sleep as t
from mss import mss
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

reply = os.getenv("REPLY_TEXT")
left = int(os.getenv("LEFT"))
top = int(os.getenv("TOP"))
width = int(os.getenv("WIDTH"))
height = int(os.getenv("HEIGHT"))

keyword1 = os.getenv("KEYWORD1_AND")
keyword2 = os.getenv("KEYWORD2_AND")
keyword3 = os.getenv("KEYWORD3_AND")
keyword4 = os.getenv("KEYWORD4_AND")
keyword5 = os.getenv("KEYWORD5_AND")

keyword6 = os.getenv("KEYWORD6_OR")
keyword7 = os.getenv("KEYWORD7_OR")

monitor = {'left': left, 'top': top, 'width': width, 'height': height}

print("Input Reply : "+reply)
print("Working System : "+platform.system())

if  platform.system()  == "Windows":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" 
elif platform.system()  == "Darwin":
    pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'

with mss() as sct:
    while True:
        screenShot = sct.grab(monitor)

        img = Image.frombytes('RGB', (screenShot.width, screenShot.height), screenShot.rgb)

        cv2.imshow('image', np.array(img))

        imageText = pytesseract.image_to_string(img, lang="chi_tra+eng", config='ㄆ')
        imageTexts = imageText.split()

        # 模糊查詢
        result1 = [i for i,x in enumerate(imageTexts) if x.find(keyword1) != -1]
        result2 = [i for i,x in enumerate(imageTexts) if x.find(keyword2) != -1]
        result3 = [i for i,x in enumerate(imageTexts) if x.find(keyword3) != -1]
        result4 = [i for i,x in enumerate(imageTexts) if x.find(keyword4) != -1]
        result5 = [i for i,x in enumerate(imageTexts) if x.find(keyword5) != -1]
        result6 = [i for i,x in enumerate(imageTexts) if x.find(keyword6) != -1]
        result7 = [i for i,x in enumerate(imageTexts) if x.find(keyword7) != -1]

        if (len(result1) > 0 and len(result2) > 0 and len(result3) > 0 and len(result4) > 0 and len(result5) > 0) and (len(result6) > 0 or len(result7) > 0):
            pyperclip.copy(reply)
            pyperclip.paste()
                            
            if  platform.system()  == "Windows":
                pyautogui.hotkey('ctrl', 'c', interval=0.1)
                pyautogui.hotkey('ctrl', 'v', interval=0)
            elif platform.system()  == "Darwin":
                pyautogui.hotkey('command', 'c', interval=0.1)
                pyautogui.hotkey('command', 'v', interval=0)
            
            pyautogui.press('enter', interval=0)

            print('Find keywords.')
            break
        else:
            print('Keyword not found.')
     

        del imageText
        del imageTexts

        if cv2.waitKey(33) & 0xFF in (
            ord('q'),
            27,
        ):
            break
