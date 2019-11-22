
import tkinter as tk
t=tk.Tk()
t.title('my home')
t.geometry('200x200')


var1=tk.StringVar()
l=tk.Label(t,bg='yellow',width=4,textvariable=var1)
l.pack()

def print_selection():
    value=lb.get(lb.curselection())   #curselection是指光标选中的值
    var1.set(value)
b1=tk.Button(t,text='print selection',width=15,height=2,command=print_selection)
b1.pack()

var2=tk.StringVar()

lb=tk.Listbox(t,listvariable=var2)      #listvariable一定不能写错
list_iteam=[11,22,33,44]
for iteam in list_iteam:
    lb.insert('end',iteam)
lb.insert(1,'first')
lb.insert(2,'second')
lb.delete(2)
lb.pack()
t.mainloop()