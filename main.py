# 一定要先装好轮子哦
#                   -- 作者：mihu
#                   -- 修改：Shio2077

import cv2                              # pip install opencv-python
import numpy                            # pip install numpy
from PIL import ImageGrab               # pip install pillow
import sys, time, ctypes                # python自带 不用安装
from random import random               # python自带 不用安装
import win32api
import os, sys

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

botm_pic = cv2.imread(resource_path('2.jpg'))
bubb_pic = cv2.imread(resource_path('3.jpg'))
THRESHOLD = 0.75


def mainLoop():
    ## 获取屏幕分辨率 for debug
    #screen = ImageGrab.grab()
    #screen_width, screen_height = screen.size
    #print(f'屏幕分辨率: {screen_width}x{screen_height}')

    # 获取对话状态截图
    #bott_pic = ImageGrab.grab(bbox=(300, 0, 500, 100))
    bott_pic = ImageGrab.grab(bbox=(0, 0, 300, 200))

    ## debug
    #bott_pic.save('bott_pic.jpg')
    
    # 匹配对话botton图片
    result_0 = cv2.matchTemplate(numpy.asarray(bott_pic), botm_pic, cv2.TM_CCOEFF_NORMED)
    max_conf_0 = cv2.minMaxLoc(result_0)  #计算匹配度0
    print('result of botton check.min_max:', max_conf_0)
    #curr_pos = win32api.GetCursorPos()  # for debug
    #print(f'当前鼠标位置: {curr_pos}')
    
    if max_conf_0[1] > THRESHOLD:
        print('处于对话状态，模拟鼠标单击')
        ctypes.windll.user32.mouse_event(2)
        time.sleep(0.05 + 0.1 * random())
        ctypes.windll.user32.mouse_event(4)
        # 在screen图片中定位与bubb_pic相似的感兴趣区域
        screen = ImageGrab.grab()
        screen_np = numpy.asarray(screen)
        result_screen = cv2.matchTemplate(screen_np, bubb_pic, cv2.TM_CCOEFF_NORMED)
        min_conf_1, max_conf_1, min_loc, max_loc = cv2.minMaxLoc(result_screen)
        #print('result of screen check.min_max:', (min_conf_1, max_conf_1, min_loc, max_loc))
        # 输出感兴趣位置的坐标
        if max_conf_1 > THRESHOLD:
            print(f'发现对话气泡，点击气泡: {max_loc}')
            # 将鼠标移动到 max_loc 位置并模拟点击
            x = int(0.5711 * max_loc[0])
            y = int(0.5711 * max_loc[1])
            ctypes.windll.user32.SetCursorPos(x + 10, y + 10)
            ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)  # 按下左键
            time.sleep(0.05 + 0.1 * random())
            ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)  # 释放左键

    
if __name__ == '__main__':
#    while True:    # for debug
#        mainLoop()
#        time.sleep(2)
    # 判断当前进程是否以管理员权限运行
    if ctypes.windll.shell32.IsUserAnAdmin() :
        print('当前已是管理员权限')
        while True:
            mainLoop()
            time.sleep(0.6 + 0.4 * random())
    else:
        print('当前不是管理员权限，以管理员权限启动新进程...')
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

