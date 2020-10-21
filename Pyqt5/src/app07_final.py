from tkinter import *
import time
import paho.mqtt.subscribe as subscribe

from colour import Color
import math
import paho.mqtt.subscribe as subscribe
import numpy as np

BLUE = Color("indigo")
MINTEMP = 22.0
MAXTEMP = 50.0
COLORDEPTH = 1024
COLORS = list(BLUE.range_to(Color("red"), COLORDEPTH))


def map_value( x_value, in_min, in_max, out_min, out_max):
    """Maps value of the temperature to color"""
    return (x_value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min





class Thera(Frame):
    msec = 90

    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self.piexls_tem = []
        self.piexls = []*64
        for i in range(64):
            self.__dict__[f'x{i}'] = DoubleVar()
            self.__dict__[f'x{i}'].set(i)
        for i in range(64):
            self.makeWidgets(i)

    def makeWidgets(self, i):
        l = Label(self, textvariable=self.__dict__[f'x{i}'], width=6, height=3)
        l.grid(row=int(i / 8), column=i % 8)

    def _update(self):
        self._setpiexls()
        self.after(self.msec, self._update)

    def _setpiexls(self):
        # self.piexls_tem = [20,25,26,27,28,29,32,64,20,25,26,27,28,29,32,64,20,25,26,27,28,29,32,64,20,25,26,27,28,29,32,64,20,25,26,27,28,29,32,64,20,25,26,27,28,29,32,64,20,25,26,27,28,29,32,64,20,25,26,27,28,29,32,64]
        self.piexls_tem = self._receiveMqtt()
        self.piexls = [COLORS[math.floor(map_value(p, MINTEMP, MAXTEMP, 0, COLORDEPTH - 1))] for p in
                       self.piexls_tem]
        for i in range(64):
            self.__dict__[f'x{i}'].set(self.piexls_tem[i])

    def _receiveMqtt(self):
        msg = subscribe.simple("test", hostname="192.168.1.120")
        msg = str(msg.payload)
        msg_list = msg.split(sep=",")
        msg_list = msg_list[1:65]
        piexls = []
        for i in msg_list:
            piexls.append(float(i))
        return piexls



    def start(self):
        self._update()
        self.pack(side=TOP)


class Watch(Frame):
    msec = 1000

    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self._running = False
        self.a = 1
        self.tem = DoubleVar()
        self.timestr1 = StringVar()
        self.timestr2 = StringVar()
        self.makeWidgets()
        self.flag = True

    def makeWidgets(self):
        l1 = Label(self, textvariable=self.tem)
        l2 = Label(self, textvariable=self.timestr2)
        l1.pack()
        l2.pack()

    def _update(self):
        self._settime()
        self.a = self.a + 1
        self.tem.set(self.a)
        self.after(self.msec, self._update)

    def _settime(self):
        today1 = str(time.strftime('%Y-%m-%d', time.localtime(time.time())))
        time1 = str(time.strftime('%H:%M:%S', time.localtime(time.time())))
        self.timestr1.set(today1)
        self.timestr2.set(time1)

    def start(self):
        self._update()
        self.pack(side=TOP)


if __name__ == '__main__':
    def main():
        root = Tk()
        root.geometry('500x500')
        frame1 = Frame(root)
        frame1.pack(side=BOTTOM)
        # mw = Watch(root)
        # mywatch = Button(frame1, text='时钟', command=mw.start)
        # mywatch.pack(side=LEFT)
        th = Thera(root)
        myth = Button(frame1, text="热成像", command=th.start)
        myth.pack(side=LEFT)
        root.mainloop()


    main()
