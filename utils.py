import pytesseract
#import pyautogui
import PIL
from PIL import Image, ImageGrab

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def retrieve_game_screenshot():
    
    screenshot = PIL.ImageGrab.grab(bbox = (1500, 150, 2000, 300))
    screenshot.show() #TESTING ONLY
    return screenshot

def process_game_screenshot():
    
    string_damage = pytesseract.image_to_string(retrieve_game_screenshot()) #returns string
    
    try:
        damage = int(string_damage)
        return damage
    
    except: #use exception to determine when damage value should be cut off.
        #while return statement is not -1, keep adding to vector. then, use largest
        #value in vector as final damage value.
        return -1
        
def get_damage():
    damage_values_retrieved = []

    # capture the initial screenshot and process it
    damage = process_game_screenshot()

    # check if the damage value exists
    while damage != -1:
        damage_values_retrieved.append(damage)
        print("Call made.")
        print(damage_values_retrieved)
        
        # capture the next screenshot and process it
        damage = process_game_screenshot()
    
    try:
        return max(damage_values_retrieved)
    
    except:
        return 0