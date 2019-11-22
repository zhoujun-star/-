
import tkinter as tk
t=tk.Tk()
t.title('my home')
t.geometry('200x200')


l=tk.Label(t,bg='yellow',width=20,text='empty')
l.pack()
def print_selection(v):
    l.config(text='you have seleced '+v)

s=tk.Scale(t,label='try me',from_=5,to=11,orient=tk.VERTICAL,length=200,showvalue=0,tickinterval=3,resolution=0.1,command=print_selection)
s.pack()
t.mainloop()
