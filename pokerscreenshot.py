from PIL import ImageGrab
import win32gui

import time

toplist, winlist = [], []
def enum_cb(hwnd, value):
    winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
win32gui.EnumWindows(enum_cb, toplist)

firefox = [(hwnd, title) for hwnd, title in winlist if 'freezeout' in title.lower()]

print(firefox)
# just grab the hwnd for first window matching firefox
firefox = firefox[0]
hwnd = firefox[0]

for i in range(10000):
    path = "screenshots"
    win32gui.SetForegroundWindow(hwnd)
    bbox = win32gui.GetWindowRect(hwnd)
    img = ImageGrab.grab(bbox)
    filename = str(i)
    time.sleep(15)
    img.save("screenshots/" + filename + ".png")