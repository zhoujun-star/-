
import tkinter as tk
t=tk.Tk()
t.title('my home')
t.geometry('200x200')


var=tk.StringVar()
l=tk.Label(t,bg='yellow',width=20,text='you have seleced')
l.pack()
def print_selection():
    l.config(text='you have seleced'+var.get())
r1=tk.Radiobutton(t,text='Option A',variable=var,relief='groove',value='A',command=print_selection)
r1.pack()
r2=tk.Radiobutton(t,text='Option B',variable=var,value='B',command=print_selection)
r2.pack()
r3=tk.Radiobutton(t,text='Option C',variable=var,value='C',command=print_selection)
r3.pack()
t.mainloop()