import tkinter as tk
t=tk.Tk()
t.title('my home')
t.geometry('200x200')

l=tk.Label(t,bg='yellow',width=20,text='empty')
l.pack()
def print_selection():
    if (var1.get()==1) & (var2.get()==0):
        l.config(text='I love Python!')
    elif (var1.get()==0) & (var2.get()==1):
        l.config(text='I love C++')
    elif (var1.get()==0) & (var2.get()==0):
        l.config(text="I don't love any")
    else:
        l.config(text='I love both')
var1=tk.IntVar()
var2=tk.IntVar()
c1 = tk.Checkbutton(t, text='Python',variable=var1,onvalue=1,offvalue=0,
                    command=print_selection, bg='lemonchiffon')
c2 = tk.Checkbutton(t, text='C++',variable=var2,onvalue=1,offvalue=0,
                    command=print_selection)
c1.pack()
c2.pack()
t.mainloop()

# from tkinter import *
# master = Tk()
#
# def var_states():
#    print("male: %d,\nfemale: %d" % (var1.get(), var2.get()))
#
# Label(master, text="Your sex:").grid(row=0, sticky=W)
# var1 = IntVar()
# Checkbutton(master, text="male", variable=var1).grid(row=1, sticky=W)
# var2 = IntVar()
# Checkbutton(master, text="female", variable=var2).grid(row=2, sticky=W)
# Button(master, text='Quit', command=master.quit).grid(row=3, sticky=W, pady=4)
# Button(master, text='Show', command=var_states).grid(row=4, sticky=W, pady=4)
# mainloop()