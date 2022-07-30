from utils import screen_size, frame, btn_locate, v_input
import cv2, time

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


count = 0
now = time.time()
time.sleep(1)
while True:
    count += 1
    fps = int(count / (time.time() - now))
    if count > 1000:
        count = 0
        now = time.time()
    print(fps)

    img,region = frame.get_frame(width, height, x, y)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    imgText = cv2.putText(img, f"FPS: {fps}", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
    cv2.imshow("Out", imgText)
    
    btn = buttonLocator.locate((region["left"],region["top"],region["width"],region["height"]),fast,img)

    if btn != None:
        vInput.press(btn)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break


# Time: 2.36 seconds
#TODO: Add FPS Counter (arg). 
#TODO: Add aption to show frame (arg).
#TODO: Add Verbose output (arg) for debugging.  
#TODO: Add arguments (arg) for fast mode and monitor choice.
#TODO: Create Documentation for setup/use (README.md & comments).