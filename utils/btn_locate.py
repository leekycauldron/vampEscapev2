import pyautogui
import threading

class ButtonLocate():
    def __init__(self):
        self.btn = None
        self.w = "./assets/w.jpg"
        self.a = "./assets/a.jpg"
        self.s = "./assets/s.jpg"
        self.d = "./assets/d.jpg"
        self.space = "./assets/space.jpg"
        self.images = [self.w, self.a, self.s, self.d, self.space]
    
    def locateImage(self,id,region):
        loc = pyautogui.locateOnScreen(self.images[id], grayscale=True, confidence=.85,region=region)
        if loc != None: self.btn = id

    def locate(self,region,fast,img):
        if fast:
            self.btn = None
            # Get Pixel Color.
            #im = pyautogui.screenshot(region=region)
            #im.save('temp.png')
            color = img[80,111]
            # Match to button.
            r = color[0]
            g = color[1]
            b = color[2]
            if r > 200 and g > 180 and b < 10:
                print("A")
                self.btn = 1
            elif r < 10 and g > 195 and b > 230:
                print("Space")
                self.btn = 4
            elif r > 210 and g < 10 and b > 90:
                print("S")
                self.btn = 2
            elif r < 50 and g > 200 and b < 10:
                print("D")
                self.btn = 3
            elif r < 10 and g < 50 and b > 230:
                print("W")
                self.btn = 0

           
        else:
            threads = []
            for i in range(5):
                t = threading.Thread(target=self.locateImage(i,region))
                #print(f"Looking for {self.images[i]}, found {loc}")
                threads.append(t)
                t.start()

            for y in threads:
                y.join()
            
            
        return self.btn