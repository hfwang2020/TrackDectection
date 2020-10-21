from tkinter import *
import time
from colour import Color
import math
import paho.mqtt.subscribe as subscribe
import numpy as np


class Watch(Frame):
    msec = 1000

    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self._running = False
        self.a =1
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
        self.a = self.a+1
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
        mw = Watch(root)
        mywatch = Button(frame1, text='时钟', command=mw.start)
        mywatch.pack(side=LEFT)

        root.mainloop()


    main()
