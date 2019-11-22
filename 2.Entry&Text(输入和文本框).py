
import tkinter as tk
t=tk.Tk()
t.title('my home')
t.geometry('200x200')

e=tk.Entry(t, show=None)
e.pack()
def insert_point():
    var=e.get()
    t1.insert('insert',var)
def insert_end():
    var=e.get()
    t1.insert('end',var)
b1=tk.Button(t,text='insert point',width=15,height=2,command=insert_point)
b2=tk.Button(t,text='insert end',command=insert_end)
b1.pack()
b2.pack()

t1=tk.Text(t,height=2)
t1.pack()

t.mainloop()