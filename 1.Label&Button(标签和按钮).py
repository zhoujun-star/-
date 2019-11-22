import tkinter as tk
t=tk.Tk()
t.title('my home')
t.geometry('200x100')



var=tk.StringVar()
l=tk.Label(t,text=var,bg='green',font=('Arial',12),width=15,height=2)
l.pack()


on_hit=False
button1 = tk.Button(t)
button1["text"]= "Hello, World!"
button1["background"] = "green"
button1.pack()
def hit_me():
    global on_hit
    if on_hit == False:
        var.set('you hit me!')
        on_hit=True
    else:
        on_hit=False
        var.set('')
b=tk.Button(t,text='hit me',width=15,height=2,command=hit_me)
b.pack()
t.mainloop()
