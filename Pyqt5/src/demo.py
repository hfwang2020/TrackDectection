from tkinter import *
from tkinter import messagebox

root = Tk()
# 调用组件的mainloop()方法，进入事件循环

root.title("fucking demo")

root.geometry("500x300+500+500")



btn01 = Button(root)
btn01["text"] = "hit me"

btn01.pack()


# e就是事件对象
def hitme(e):
    messagebox.showinfo("message", "u fuck hit me")
    print("fuck u idiot")


btn01.bind("<Button-1>", hitme)

root.mainloop()
