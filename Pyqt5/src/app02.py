#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:洪卫

import tkinter as tk  # 使用Tkinter前需要先导入
from colour import Color
import math
# 第1步，实例化object，建立窗口window
window = tk.Tk()

# 第2步，给窗口的可视化起名字
window.title('My Window')

# 第3步，设定窗口的大小(长 * 宽)
window.geometry('800x800')  # 这里的乘是小x

# 第4步，在图形界面上设定标签
BLUE = Color("indigo")
# low range of the sensor (this will be blue on the screen)
MINTEMP = 22.0
# high range of the sensor (this will be red on the screen)
MAXTEMP = 40.0
COLORDEPTH = 1024
COLORS = list(BLUE.range_to(Color("red"), COLORDEPTH))

def map_value(x_value, in_min, in_max, out_min, out_max):
    """Maps value of the temperature to color"""
    return (x_value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
PIXELS_TEM = [22,30,35,39.9]

PIXELS = [COLORS[math.floor(map_value(p, MINTEMP, MAXTEMP, 0, COLORDEPTH - 1))] for p in PIXELS_TEM]

l11 = tk.Label(window, text='1',bg=str(PIXELS[0].get_hex()), width=10, height=5)
l12 = tk.Label(window, text='2',bg=str(PIXELS[1].get_hex()), width=10, height=5)
l13 = tk.Label(window, text='3',bg=str(PIXELS[2].get_hex()), width=10, height=5)
l14 = tk.Label(window, text='4',bg=str(PIXELS[3].get_hex()), width=10, height=5)
l15 = tk.Label(window, text='5',bg=str(PIXELS[4].get_hex()), width=10, height=5)
l16 = tk.Label(window, text='6',bg=str(PIXELS[5].get_hex()), width=10, height=5)
l17 = tk.Label(window, text='7',bg=str(PIXELS[6].get_hex()), width=10, height=5)
l18 = tk.Label(window, text='8',bg=str(PIXELS[7].get_hex()), width=10, height=5)

# 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高

# 第5步，放置标签


# l11.grid(row=1, column=1)
# l12.grid(row=1, column=2)
# l13.grid(row=1, column=3)
# l14.grid(row=1, column=4)
# l15.grid(row=1, column=5)
# l16.grid(row=1, column=6)
# l17.grid(row=1, column=7)
# l18.grid(row=1, column=8)

# 第6步，主窗口循环显示
window.mainloop()
# 注意，loop因为是循环的意思，window.mainloop就会让window不断的刷新，如果没有mainloop,就是一个静态的window,传入进去的值就不会有循环，mainloop就相当于一个很大的while循环，有个while，每点击一次就会更新一次，所以我们必须要有循环
# 所有的窗口文件都必须有类似的mainloop函数，mainloop是窗口文件的关键的关键。
