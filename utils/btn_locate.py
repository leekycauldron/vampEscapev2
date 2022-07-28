import pyautogui
import threading

class ButtonLocate():
    def __init__(self):
        self.w = "./assets/w.jpg"
        self.a = "./assets/a.jpg"
        self.s = "./assets/s.jpg"
        self.d = "./assets/d.jpg"
        self.space = "./assets/space.jpg"
        self.images = [self.w, self.a, self.s, self.d, self.space]

    def locate(self,region):
        for i in range(5):
            #TODO: Make this threaded
            loc = pyautogui.locateOnScreen(self.images[i], grayscale=True, confidence=.5,region=region)
            #print(f"Looking for {self.images[i]}, found {loc}")
            if loc != None:
                return i