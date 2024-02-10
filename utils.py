import pytesseract
#import pyautogui
import PIL
from PIL import Image, ImageGrab

pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def retrieve_game_screenshot():
    
    screenshot = PIL.ImageGrab.grab(bbox = (1500, 90, 1800, 400))
    #screenshot.show() #TESTING ONLY
    return screenshot

def process_game_screenshot():
    
    string_damage = pytesseract.image_to_string(retrieve_game_screenshot()) #returns string
    
    try:
        damage = int(string_damage)
        return damage
    except: #use exception to determine when damage value should be cut off.
        #while return statement is not -1, keep adding to vector. then, use largest
        #value in vector as final damage value.
        print("Error converting string_dps value to int.")
        return -1
        
def get_damage():
    #print(process_game_screenshot()) #TESTING ONLY

    #initialize empty array for every character attack instance.
    damage_values_retrieved = []

    while process_game_screenshot() != -1:
        damage_values_retrieved.append(process_game_screenshot())
        print("Call made.") #TESTING ONLY
        print(damage_values_retrieved) #TESTING ONLY
    return max(damage_values_retrieved)
    #RETURN WHEN DONE.