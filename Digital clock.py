from tkinter import *
import time as t

dc = Tk()
dc.title("DIGITAL CLOCK ")
dc.geometry("500x100")


def time():
    d = t.strftime("%d-%m-%Y , %H:%M:%S %p")
    l.config(text=d)
    l.after(1000, time)


l = Label(dc, font=('Arial', 25), bg="black", fg="yellow")
l.pack()
time()
mainloop()
