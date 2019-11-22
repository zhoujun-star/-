import tkinter as tk
t=tk.Tk()
t.title('My windows')
t.geometry('200x200')

tk.Label(t,text='on the windows').pack()

frm=tk.Frame(t)
frm.pack()
frm_l=tk.Frame(frm)
frm_r=tk.Frame(frm)
frm_l.pack(side='left')
frm_r.pack(side='right')
tk.Label(frm_l,text='on the frm_l').pack()
tk.Label(frm_r,text='on the frm_r').pack()
tk.Label(frm_l,text='on the frm_r').pack()
t.mainloop()