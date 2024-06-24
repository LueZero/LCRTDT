# Line Chat Room Text Detection Transponder(命令模式版)

偵測 `LINE 聊天室` 關鍵文字來自動回覆訊息。

## Initialization

1. Copy the env example to .env and set relevant parameters.

2. Install dependent packages : `pip or pip3 install -r requirements.txt`.

3. tesseract installation confirmation and setting chi_tra.traineddata.

## Execution

1. Command line run `python main.py` or `python3 main.py`.

## Cautions

### Tesseract OCR

* 命令模式下執行程式 `tesseract` 需要手動安裝檔案，安裝連結 <a href="https://tesseract-ocr.github.io/tessdoc/Installation.html">tesseract-ocr 官網 </a>。

###  Windows

*  把中文模型(chi_tra.traineddata)放入位置 `tesseract` 安裝路徑。

    ```
    Windows ex: C:\Program Files\Tesseract-OCR\tessdata\chi_tra.traineddata 
    ```
### MacOS

* 把中文模型(chi_tra.traineddata)放入位置 `tesseract` 安裝路徑。
   
   ```
   MacOS ex: /usr/local/Cellar/tesseract/3.05.02[版本號]/share/tessdata
   ```

* 若鍵盤指令(pyautogui)無效，請記得去看隱私權設定是否給權限。

