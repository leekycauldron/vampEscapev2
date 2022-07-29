import numpy as np
import cv2
from mss import mss
from PIL import Image

class Frame():
    def __init__(self) -> None:
        pass
    
    def get_frame(self, width, height, x, y):
        # left: move to halfway point then go left 1/20 of screen
        # top: move 80% of the screen size down then go up 1/10 of screen
        # width: 1/10 of screen size
        # height: 1/10 of screen size
        # NOTE: Percentages are used to allow for different screen sizes.
        bounding_box = {'top': int(0.8*height)-int(0.1*height)+y, 'left': int(0.5*width)-int(0.05*width)+x, 'width': int(0.1*width), 'height': int(0.1*height)}
        sct = mss()
        sct_img = sct.grab(bounding_box)
        return np.array(sct_img), bounding_box
        