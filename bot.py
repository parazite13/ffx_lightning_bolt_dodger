__author__ = 'Ugrend'
import win32gui
import keyboard
import time
# https://msdn.microsoft.com/en-us/library/dd375731?f=255&MSPPError=-2147217396 for keys

KEY_C = 0x43
x_pixel = 1915 # X cord of pixel to look at , im looking at top right of screen in the clouds
y_pixel = 213  # Y cord

time.sleep(3) # give me time to get ffx in focus
print "BOT STARTED"
dodge_count = 0

while True:
    try:
        color = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), x_pixel , y_pixel)
        if color > 11000000:
            print color
            print "LIGHTNING"
            dodge_count +=1
            print dodge_count
            keyboard.PressKey(KEY_C)
            time.sleep(1)
            keyboard.ReleaseKey(KEY_C)
            time.sleep(2)
    except:
        pass
