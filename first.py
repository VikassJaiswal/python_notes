from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from tkinter.ttk import Progressbar 
import os
import time

window=Tk()
window.title("vikas")
window.config(bg="lightblue")
w=window.winfo_screenwidth()
h=window.winfo_screenheight()
sw=window.winfo_screenwidth()
sh=window.winfo_screenheight()
wpos=(sw/2)-(w/2)
hpos=(sh/2)-(h/2)
#window.geometry("%dx%d+%d+%d"%(wpos,hpos,w,h))
window.geometry("%dx%d"%(sw,sh))
window.maxsize(1200,1200)
window.minsize(1100,1000)

def display():
    for i in range(1,11):
        window.update_idletasks()
        p["value"]+=10
        time.sleep(0.5)
        l1["text"]=p["value"],"%"
    window.destroy()
    os.system("second.py")



image=Image.open("vaccine.jpg")
resize_image=image.resize((1200,700))
img=ImageTk.PhotoImage(resize_image)
l2=Label(image=img)
l2.image=img
l2.pack()
l2.place(x=0,y=0)

l=Label(window,text="VACCINATION",font=("comic sans ms",50,"bold","underline"))
l.config(bg="white",fg="black")
l.place(x=300,y=40)

l1=Label(window,font=("comic sans ms",15,"bold","underline"))
l1.config(bg="white",fg="black")
l1.place(x=750,y=500)


p=Progressbar(window,orient=HORIZONTAL,length=300,mode="determinate",value=0)
p.place(x=410,y=500)
display()

window.mainloop()
