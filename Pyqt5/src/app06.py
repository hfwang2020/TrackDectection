import tkinter,datetime
def uptime():

    global TimeLabel
    TimeLabel["text"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S:') + "%d" %(datetime.datetime.now().microsecond // 100000)
    win.after(100,uptime)

win = tkinter.Tk()
win.title("当前时间")
win.attributes("-topmost",True)
win.geometry("%dx%d" %(200,50))
TimeLabel = tkinter.Label(text = "%s%d" %(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S:'),datetime.datetime.now().microsecond // 100000))
TimeLabel.pack(fill=tkinter.BOTH,padx = 10,pady = 8)
win.after(100,uptime)
win.mainloop()