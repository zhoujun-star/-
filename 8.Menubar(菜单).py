import tkinter as tk
t=tk.Tk()
t.title('my home')
t.geometry('200x200')

l=tk.Label(t,text='',bg='green')
l.pack()

counter=0
def do_job():
    global counter
    l.config(text='do '+ str(counter))
    counter=counter+1

menubar=tk.Menu(t)
filemenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='New',command=do_job)
filemenu.add_command(label='Open',command=do_job)
filemenu.add_command(label='Save',command=do_job)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=t.quit)


editmenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='Edit',menu=editmenu)
editmenu.add_command(label='Cut',command=do_job)
editmenu.add_command(label='Copy',command=do_job)
editmenu.add_command(label='Paste',command=do_job)

submenu=tk.Menu(filemenu,tearoff=0)
filemenu.add_cascade(label='Import',menu=submenu,underline=0)
submenu.add_command(label='Submenu',command=do_job)
t.config(menu=menubar)

t.mainloop()