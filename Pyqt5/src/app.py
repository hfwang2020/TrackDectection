
from tkinter import *
from tkinter import messagebox

class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.createWidget()

    def createWidget(self):
        self.btn01 = Button(self)
        self.btn01["text"] = "hit me"
        self.btn01.pack()
        self.btn01["command"] = self.hitme

        self.btnQuit = Button(self,text="quitzero",command =root.destroy)
        self.btnQuit.pack()

    def hitme(self):
        messagebox.showinfo("message", "u fuck hit me")

if __name__== '__main__':
    root = Tk()
    root.geometry("400x400+400+400")
    root.title("GUI")
    app = Application(master = root)
    root.mainloop()
