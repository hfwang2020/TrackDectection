from tkinter import *
import time
from colour import Color
import math
import paho.mqtt.subscribe as subscribe
import numpy as np

BLUE = Color("indigo")
MINTEMP = 22.0
MAXTEMP = 60.0
COLORDEPTH = 1024
COLORS = list(BLUE.range_to(Color("red"), COLORDEPTH))


class StopWatch(Frame):
    '''实现一个秒表部件'''
    msec = 5

    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self._start = 0.0
        self._elapsedtime = 0.0
        self._running = False
        self.timestr = StringVar()
        self.makeWidgets()
        self.flag = True

    def makeWidgets(self):
        l = Label(self, textvariable=self.timestr)
        self._setTime(self._elapsedtime)
        l.pack(fill=X, expand=NO, pady=2, padx=2)

    def _update(self):
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(self.msec, self._update)

    def _setTime(self, elap):
        '''将时间格式改为 分：秒：百分秒'''
        minutes = int(elap / 60)
        seconds = int(elap - minutes * 60.0)
        hseconds = int((elap - minutes * 60.0 - seconds) * 100)
        self.timestr.set('%2d:%2d:%2d' % (minutes, seconds, hseconds))

    def Start(self):
        if not self._running:
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = True

    def Stop(self):
        '''停止秒表'''
        if self._running:
            self.after_cancel(self._timer)
            self._elapsedtime = time.time() - self._start
            self._setTime(self._elapsedtime)
            self._running = False

    def Reset(self):
        '''重设秒表'''
        self._start = time.time()
        self._elapsedtime = 0.0
        self._setTime(self._elapsedtime)

    def stopwatch(self):
        if self.flag == True:
            self.pack(side=TOP)
            Button(self, text='start', command=self.Start).pack(side=LEFT)
            Button(self, text='stop', command=self.Stop).pack(side=LEFT)
            Button(self, text='reset', command=self.Reset).pack(side=LEFT)
            Button(self, text='quit', command=self.quit).pack(side=LEFT)
        self.flag = False


class Thera(Frame):
    mesc = 10

    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self.__running = False
        self.piexls_tem = []
        self.tem = StringVar()
        # for i in range(0,4):
        #     self.piexls_tem[i] = DoubleVar()
        self.piexls = [BLUE] * 64

        self.makeWidgets()

        self.flag = True

    def makeWidgets(self):
        l1 = Label(self, text=self.tem, width=10, height=5)
        l1.pack()
        # l1 = Label(self, text=str(self.piexls_tem[i]),  width=10, height=5)
        # l1.grid(row=int((i ) / 2), column=(i ) % 2)

    def _update(self):
        self._setpiexls()
        self.timer = self.after(self.mesc, self._update)

    def _setpiexls(self):
        a = int(self.tem.get())
        a = a + 1
        self.tem.set(str(a))
        # for i in range(0,4):
        #     a = self.piexls_tem[i].get()
        #     a = a+1
        #     self.piexls_tem[i].set(a)
        # msg = subscribe.simple("test", hostname="192.168.1.102")
        # self.piexls_tem = self.messageToArray(str(msg.payload))
        # self.piexls = [COLORS[math.floor(self.map_value(p, MINTEMP, MAXTEMP, 0, COLORDEPTH - 1))] for p in
        #                self.piexls_tem]
        # self.piexls = [COLORS[math.floor(self.map_value(p, MINTEMP, MAXTEMP, 0, COLORDEPTH - 1))] for p in self.piexls_tem]

    def map_value(self, x_value, in_min, in_max, out_min, out_max):
        """Maps value of the temperature to color"""
        return (x_value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def messageToArray(self, msg):
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
    msec = 1

    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self._running = False
        self.timestr1 = StringVar()
        self.timestr2 = StringVar()
        self.makeWidgets()
        self.flag = True

    def makeWidgets(self):
        l1 = Label(self, textvariable=self.timestr1)
        l2 = Label(self, textvariable=self.timestr2)
        l1.pack()
        l2.pack()

    def _update(self):
        self._settime()
        self.timer = self.after(self.msec, self._update)

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
        # sw = StopWatch(root)
        # stpwtch = Button(frame1, text='秒表', command=sw.stopwatch)
        # stpwtch.pack(side=RIGHT)
        mw = Watch(root)
        mywatch = Button(frame1, text='时钟', command=mw.start)
        mywatch.pack(side=LEFT)
        mt = Thera(root)
        myth = Button(frame1, text='热成像', command=mt.start)
        myth.pack(side=LEFT)
        root.mainloop()


    main()
