import pydirectinput

class VirtualInput():
    def __init__(self) -> None:
        self.keys = ['w', 'a', 's', 'd', 'space']
    def press(self, key):
        pydirectinput.press(self.keys[key])
