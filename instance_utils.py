import pyautogui
import pygetwindow


def find_window():
    for window in pygetwindow.getAllTitles():
        if "Honkai: Star Rail" in window:
            return pygetwindow.getWindowsWithTitle(window)[0]
        
def main():

    honkai_window = find_window()

    if honkai_window:
        print("Found Star Rail Window") #TESTING ONLY
    else:
        print("Instance not found.") 
    
main()