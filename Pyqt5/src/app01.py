
from tkinter import *
from tkinter import messagebox

class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.createWidget()

    def createWidget(self):
        self.label01 = Label(self,text="1",width =4,height =2,bg="green",
                             padx=0,pady=0)
        self.label01.pack()
        self.label02 = Label(self, text="2", width=4, height=2, bg="green",
                             padx=8, pady=8)
        self.label02.pack()


if __name__== '__main__':
    root = Tk()
    root.geometry("800x800+400+400")
    root.title("GUI")
    app = Application(master = root)
    root.mainloop()
