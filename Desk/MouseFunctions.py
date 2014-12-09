import win32api, win32con
import time
import math

win = win32api

def move(x,y):
    #click, rightClick, press, rightPress, release, rightRelease, move
    win.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0)

def click():
    win.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

def rClick():
    win.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
    win.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)

def press():
    win.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)

def rPress():
    win.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)

def release():
    win.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

def rRelease():
    win.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
    
