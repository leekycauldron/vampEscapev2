from numpy import str0


class ScreenSize():
    def __init__(self):
        self.h = 0
        self.w = 0   
        self.x = 0 # for offsets
        self.y = 0 # for offsets

    def get_screen_size(self):
        from screeninfo import get_monitors
        screens = []
        for m in get_monitors():
            screens.append(m)
        if len(screens) == 1:
            self.h = screens[0].height
            self.w = screens[0].width
            self.x = screens[0].x
            self.y = screens[0].y
            print("Screen size is:", str(self.w), "x", str(self.h)+'.')
        else:
            print("Multiple screens detected. Please select the screen you want to use.")
            for i in range(len(screens)):
                print(f"[{i+1}] - Name: {screens[i].name}, Width: {screens[i].width}, Height: {screens[i].height}")
            x = int(input("Select screen: "))
            self.h = screens[x-1].height
            self.w = screens[x-1].width
            self.x = screens[x-1].x
            self.y = screens[x-1].y
            print(f"Option {x} selected. Screen size is:", str(self.w), "x", str(self.h)+'.')
    
    def get_screen_height(self):  
        return self.h
    
    def get_screen_width(self):
        return self.w
    
    def get_x_offset(self):
        return self.x
    
    def get_y_offset(self):
        return self.y
