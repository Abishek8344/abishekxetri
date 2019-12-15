#simple calculator
from tkinter import *
expression =" "
def press(num):
    global expression
    expression=expression+str(num)
    equation:set(expression)
def clear():
    global expression
    expression=" "
    equation.set(expression)
def equalpress():
    try:
        global expression
        total=str(eval(expression))
        equation.set(total)
        expressions=" "
    except:
        equation.set("error")
        expression=" "
root=Tk()
root.title('calculator')
root.geometry('500x500')
root.resizable(1,1)
root.config(bg='blue')
equation=StringVar()

expression_field=Entry(root,textvariable=equation)
expression_field.place(relx=0.02,rely=0.02,height=70,width=350)

button1=Button(root,text='1',command=lambda:press(1),height=4,width=8)
button1.place(relx=0.02,rely=0.18)
button2=Button(root,text='2',command=lambda:press(2),height=4,width=8)
button2.place(relx=0.20,rely=0.18)
root.mainloop()