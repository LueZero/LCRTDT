#coding=utf-8

import os
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

mon = {'left': 0, 'top': 0, 'width': 400, 'height': 500}

# Windows 注意事項
# C:\Program Files\Tesseract-OCR\tessdata\chi_tra.traineddata 把中文模型放入此位置，看你OCR安裝位置

# MacOS 注意事項
# /usr/local/Cellar/tesseract/3.05.02[版本號]/share/tessdata 把中文模型放入此位置
# 鍵盤指令無效記得去看隱私權設定

print("輸入文字:"+reply)
print("作業系統:"+platform.system())

if  platform.system()  == "Windows":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" 
elif platform.system()  == "Darwin":
    pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'

with mss() as sct:
    while True:
        screenShot = sct.grab(mon)

        img = Image.frombytes(
            'RGB',
            (screenShot.width, screenShot.height),
            screenShot.rgb,
        )

        cv2.imshow('test', np.array(img))

        data = pytesseract.image_to_string(img, lang="chi_tra+eng", config='ㄆ')

        result = data.split()

        a = [i for i,x in enumerate(result) if x.find('招募') != -1]
        b = [i for i,x in enumerate(result) if x.find('自') != -1]
        c = [i for i,x in enumerate(result) if x.find('假') != -1]
        d = [i for i,x in enumerate(result) if x.find('採') != -1]
        e = [i for i,x in enumerate(result) if x.find('檢') != -1]
        f = [i for i,x in enumerate(result) if x.find('六') != -1]
        g = [i for i,x in enumerate(result) if x.find('日') != -1]

        if len(a) > 0 and len(b) > 0 and len(c) > 0 and len(d) > 0 and len(e) > 0:
            if len(f) > 0 or len(g) > 0:
                pyperclip.copy(reply)
                pyperclip.paste()
                                
                pyautogui.hotkey('command', 'c', interval=0.25)
                pyautogui.hotkey('command', 'v', interval=0.25)
                pyautogui.press('enter', interval=0.25)

                print('找到關鍵字')
                break
            else:
                print('找不到關鍵字')
        else:
            print('找不到關鍵字')

        del data

        if cv2.waitKey(33) & 0xFF in (
            ord('q'),
            27,
        ):
            break
