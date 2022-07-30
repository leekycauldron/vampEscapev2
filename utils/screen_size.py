class ScreenSize():
    def __init__(self):
        self.h = 0
        self.w = 0   
        self.x = 0 # for offsets
        self.y = 0 # for offsets
        self.fast = False

    def get_screen_size(self,monitor=None,mode=None):
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
            x = 0
            if monitor is not None:  # If the user specified a monitor in arg.
                if monitor > len(screens) or monitor < 1:
                    print("Error: Invalid monitor number.")
                    exit()
       
                x = int(monitor)

            else:
                print("Multiple screens detected. Please select the screen you want to use.")
                for i in range(len(screens)):
                    print(f"[{i+1}] - Name: {screens[i].name}, Width: {screens[i].width}, Height: {screens[i].height}")
                while True:
                    try:
                        x = int(input("Select screen: "))
                        if x > len(screens) or x < 1:
                            print("Invalid selection.")
                            continue
                        break
                    except ValueError:
                        print("Invalid selection.")
                        continue
            self.h = screens[x-1].height
            self.w = screens[x-1].width
            self.x = screens[x-1].x
            self.y = screens[x-1].y
            print(f"Option {x} selected. Screen size is:", str(self.w), "x", str(self.h)+'.')

            if mode is not None:
                print("Entering fast escape program.")
                self.fast = True
                return
            fast = input("Do you want to enable fast mode? (Unstable) [y/n]: ")
            if fast.lower() == "n":
                print("Entering regular escape program.")
                return False
            elif fast.lower() == "y" or fast.lower() == "":
                print("Entering fast escape program.")
                self.fast = True
            else:
                print("Invalid selection. Entering regular escape program.")

    
    def get_screen_height(self):  
        return self.h
    
    def get_screen_width(self):
        return self.w
    
    def get_x_offset(self):
        return self.x
    
    def get_y_offset(self):
        return self.y
    
    def get_fast_mode(self):
        return self.fast
