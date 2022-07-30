from utils import logger, screen_size, frame, btn_locate, v_input
import cv2, time
import argparse

# Construct the argument parser and parse command line arguments.
ap = argparse.ArgumentParser(description="Options for the escape program. Check the README for more information.")

ap.add_argument("-f","--fps",nargs='?',const='',required=False,help="Show FPS Counter (Must have --image on).")
ap.add_argument("-i","--image",nargs='?',const='',required=False,help="Show Image being processed. (Has some impact on performance.)")
ap.add_argument("-v","--verbose",nargs='?',const='',required=False,help="Verbose output for debugging.")
ap.add_argument('-m','--monitor',type=int,default=None,required=False,help="Monitor to use for capture. (Options are shown when progam is ran and is able to be chosen at runtime unless specified here.)")
ap.add_argument('-fm','--mode',nargs='?',const='',required=False,help="Enable for fast mode (fast, unstable?).")
args = vars(ap.parse_args())

if args["fps"] is not None and args["image"] is None: 
    print("Error: --fps requires --image.")
    exit()


size_finder = screen_size.ScreenSize()
size_finder.get_screen_size(args["monitor"],args["mode"])
fast = size_finder.get_fast_mode()

width = size_finder.get_screen_width()
height = size_finder.get_screen_height()
x = size_finder.get_x_offset()
y = size_finder.get_y_offset()

log = logger.Logger()

buttonLocator = btn_locate.ButtonLocate(log)
vInput = v_input.VirtualInput()

frame = frame.Frame()




count = 0
now = time.time()
delay  = time.time() # used to print fps every x seconds on verbose output.
print('NOTE: Keep this program running in the background while playing the game!')
time.sleep(1)

    
while True:
    img,region = frame.get_frame(width, height, x, y)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


    # Calculate FPS.
    count += 1
    fps = int(count / (time.time() - now))
    # Reset frame count every 1000 frames rendered.
    if count > 1000:
        count = 0
        now = time.time()
    if time.time() - delay > 2:
        delay = time.time()
        log.log(f"FPS: {fps}",args["verbose"])
    
    if args["image"] is not None:
        if args["fps"] is not None:
            imgText = cv2.putText(img, f"FPS: {fps}", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
        else:
            imgText = img
        
        cv2.imshow("Out", imgText)
    
    btn = buttonLocator.locate((region["left"],region["top"],region["width"],region["height"]),fast,img,args["verbose"])

    if btn != None:
        vInput.press(btn)
    
    if args["image"] is not None:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


# Recorded Escape Time(s): 2.36 seconds.

#TODO: Create Documentation for setup/use (README.md & comments).