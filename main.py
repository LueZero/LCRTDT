import os
import numpy as np
import pytesseract
import operator
import cv2
import re
import pyautogui
import pyperclip

from mss import mss
from PIL import Image
from dotenv import load_dotenv
load_dotenv()

reply = os.getenv("REPLY_TEXT")

mon = {'left': 0, 'top': 350, 'width': 500, 'height': 600}

keywords = ['招募', '自', '假', '採', '六', '日']

# Tesseract-OCR\tessdata\chi_tra.traineddata 把中文模型放入此位置

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

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

        print(keywords)

        a = [i for i,x in enumerate(result) if x.find('招募') != -1]
        b = [i for i,x in enumerate(result) if x.find('自') != -1]
        c = [i for i,x in enumerate(result) if x.find('假') != -1]
        d = [i for i,x in enumerate(result) if x.find('採') != -1]
        e = [i for i,x in enumerate(result) if x.find('檢') != -1]
        f = [i for i,x in enumerate(result) if x.find('六') != -1]
        g = [i for i,x in enumerate(result) if x.find('日') != -1]

        if len(a) > 0 and len(b) > 0 and len(c) > 0 and len(d) > 0 and len(e) > 0:
            if len(f) > 0 or len(g) > 0:
                print('找到關鍵字')
                pyperclip.copy(reply)
                pyperclip.paste()
                pyautogui.hotkey('ctrl', 'c')
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.press('enter')
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
