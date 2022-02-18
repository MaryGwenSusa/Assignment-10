import cv2 # Access to the Default Cam for scanning
import pyzbar.pyzbar as pyzbar
import datetime

def scannerSetUp(frame):
    codeToBeRead = pyzbar.decode(frame)
    for qrcode in codeToBeRead:
        r, e , c, t = qrcode.rect

        # Rectangle Frame detecting the code
        infoQRCode = qrcode.data.decode('utf-8') # ASCII Standard Unicode Character
        cv2.rectangle(frame, (r, e),(r+c, e+t), (0, 255, 0), 3) # ASCII Font Density 
        
        # Shows decoded data
        scannerFont = cv2.FONT_HERSHEY_COMPLEX_SMALL # Change font type
        cv2.putText(frame, infoQRCode, (r + 6, e - 6), scannerFont, 1.0, (0, 0, 255), 3) # Layout and text color