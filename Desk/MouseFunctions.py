import win32api, win32con
import time
import math

win = win32api

def moveMouse(x, y):
    (x_prev, y_prev) = win.GetCursorPos()
    win.SetCursorPos((x+x_prev, y+y_prev))

def rightClick():
    win.mouse_event(win32con.MOUSEEVENTF_MOVE, 100, 100, 0, 0)
