import cv2
import pytesseract
import pyautogui
import time
import PIL
from PIL import Image, ImageGrab

pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def retrieve_dps_screenshot():
    
    screenshot = PIL.ImageGrab.grab(bbox = (1500, 90, 1800, 400))
    screenshot.show()
    return screenshot

def process_dps_screenshot():
    
    string_dps = pytesseract.image_to_string(retrieve_dps_screenshot()) #returns string
    
    try:
        dps = int(string_dps)
        return dps
    except:
        print("Error converting string value to int.")
        
print(process_dps_screenshot()) #TESTING ONLY