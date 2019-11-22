
import tkinter as tk
t=tk.Tk()
t.title('my home')
t.geometry('200x200')

canvas=tk.Canvas(t,bg='blue',height=100,width=200)
image_file=tk.PhotoImage=('123.gif')
image=canvas.create_image(10,10,anchor='nw')
rect=canvas.create_rectangle(20,20,40,40)
canvas.pack()
def haha():
    canvas.move=(rect,0,444)
b=tk.Button(t,text='兄弟！！@#！@#',command=haha)
b.pack()

t.mainloop()