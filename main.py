from utils import screen_size, frame, btn_locate, v_input
import cv2

size_finder = screen_size.ScreenSize()
size_finder.get_screen_size()
fast = size_finder.get_fast_mode()

width = size_finder.get_screen_width()
height = size_finder.get_screen_height()
x = size_finder.get_x_offset()
y = size_finder.get_y_offset()

buttonLocator = btn_locate.ButtonLocate()
vInput = v_input.VirtualInput()

frame = frame.Frame()

while True:
    img,region = frame.get_frame(width, height, x, y)
    cv2.imshow("Test", img)
    
    btn = buttonLocator.locate((region["left"],region["top"],region["width"],region["height"]),fast)

    if btn != None:
        vInput.press(btn)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break


#TODO: Add FPS Counter (arg).
#TODO: Add aption to show frame (arg).
#TODO: Add Verbose output (arg) for debugging.  
#TODO: Add arguments (arg) for fast mode and monitor choice.
#TODO: Create Documentation for setup/use (README.md & comments).