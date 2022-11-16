#刷屏工具v1.1 by.taskmgrTZT
#1.0 经测试,工具可以正常使用
#1.1 删除不必要库

import time
import pyperclip
import win32api
from pykeyboard import *
from pykeyboard import PyKeyboard


pyperclip.copy("在")   #修改输出内容

k = PyKeyboard()

print("三秒后开始刷屏")

time.sleep(3)   #在3秒后开始

for i in range(50):  #修改执行次数
    k.press_key(k.control_key)
    k.tap_key('v')
    k.release_key(k.control_key)
    time.sleep(0.05)
    win32api.keybd_event(13,0,0,0)