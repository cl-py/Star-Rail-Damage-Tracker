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
#TESSERACT INSTALLATION REQUIRED
def process_dps_screenshot():
    dps = pytesseract.image_to_string(retrieve_dps_screenshot())
    return dps
print(process_dps_screenshot())