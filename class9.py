from tkinter import *
def click():
    txt.set("you clicked here")
root=Tk()
root.title("my window")
txt=StringVar()
txt.set("shit")
root.geometry("500x400")
var=Label(root,text="welcome to the sanity")
var.place(relx=0,rely=0.5)
var2=Label(root,textvariable=txt)
var2.place(relx=0.5,rely=0.5)
var2.config(font=("Times New Roman",10),background="black",fg="red")
but1=Button(root,text="click here",font=("",10),command=click)
but1.place(relx=0.5,rely=0.6)
root.resizable(0,0)
root.config(background="blue")
root.mainloop()