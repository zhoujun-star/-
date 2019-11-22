from tkinter import *
from tkinter import ttk
import os, shutil, time, subprocess
import tkinter.filedialog
from tkinter import messagebox
class FileDoing(object):
    def __init__(self):
        self.t = Tk()
        self.t.title('文件检索')
        self.t.iconbitmap('11.ico')
        self.t.geometry('800x600')
        # self.t.resizable(False, False)
        self.tree = None
        self.top = None
        self.name = StringVar()
        self.path = StringVar()
        self.type = StringVar()
        self.num_Var = StringVar()
        self.num_Var.set('待检索')
        self.file_name = []
        self.need_filepath = []
        self.drives = []
        self.path_find = []
        self.selcte = {'one_week':[],'one_month':[],'three_month':[],'better_longer':[]}
        self.classfication = {'所有类型': ['.txt', '.doc', '.xl8', '.ppt', '.docx', '.xlsx', '.pptx', '.pdf', '.hlp', '.wps', '.xtf', '.htal','.jpg', '.png', '.tiff', '.swf', '.bmp', '.gif', '.pio', '.png''.tif','.flv', '.zmvb', '.mp4', '.mvb''.avi', '.mpE', '.mov', '.Wsf','.wma', '.mp3', '.wav', '.aif', '.au', '.ram', '.mmf', '.amr', '.ncm', ',aac', '.flac','.int', '.sys', '.dll', '.adt', '.nip', '.rar', '.arj', '.go..', '.zip', '.exe''.com', '.asmfor', '.lib', '.lst', '.msE', '.obj', '.pss', '.wki', '.bas', 'jasa', '.map', 'iso', '.IDF', '.mdb', '.mdf', '.DB', '.DBP', '.wdb'],
            '文本文件': ['.txt', '.doc', '.xl8', '.ppt', '.docx', '.xlsx', '.pptx', '.pdf', '.hlp', '.wps', '.xtf',
                     '.htal'],
            '图片文件': ['.jpg', '.png', '.tiff', '.swf', '.bmp', '.gif', '.pio', '.png''.tif'],
            '视频文件': ['.flv', '.zmvb', '.mp4', '.mvb''.avi', '.mpE', '.mov', '.Wsf'],
            '音频文件': ['.wma', '.mp3', '.wav', '.aif', '.au', '.ram', '.mmf', '.amr', '.ncm', ',aac', '.flac'],
            '系统文件': ['.int', '.sys', '.dll', '.adt'],
            '压缩文件': ['.nip', '.rar', '.arj', '.go..', '.zip'],
            '可执行文件': ['.exe''.com'],
            '程序源文件': ['.asmfor', '.lib', '.lst', '.msE', '.obj', '.pss', '.wki', '.bas', 'jasa'],
            '映像文件': ['.map', 'iso'],
            '数据库文件': ['.IDF', '.mdb', '.mdf', '.DB', '.DBP', '.wdb']}
        self.CreateWidget()
    def CreateWidget(self):

        # 条件填写区域
        f1 = LabelFrame(self.t, text='条件区域')
        f1.pack(pady='10', fill="both")
        im_1 = PhotoImage(file='12.png')
        im_2 = PhotoImage(file='13.png')
        self.f1_Lname = Label(f1, text='关键字:', font=('黑体',10))
        self.f1_Lname.pack(anchor='w',side='left', padx='5')
        self.f1_Rname = Entry(f1, widt=17, textvariable=self.name,font=('黑体',12))
        self.f1_Rname.pack(side='left', fill=X,expand=YES)
        self.f1_Lpath = Label(f1, text='源路径:', font=('黑体',10))
        self.f1_Lpath.pack(side='left',  padx='5')
        self.f1_Rpath = Entry(f1, widt=20, textvariable=self.path,font=('黑体',12))
        self.f1_Rpath.pack(side='left',fill=X,expand=YES)
        self.button = Button(f1, text='...', image=im_1,bd=0,font=('黑体',9), command=self.Path)
        self.button.pack(side='left')
        self.f1_Ltype = Label(f1, text='选类型:', font=('黑体',10))
        self.f1_Ltype.pack(side='left', padx='5')
        self.f1_Rtype = ttk.Combobox(f1,textvariable=self.type, width=9,state = 'readonly')
        self.f1_Rtype["values"] = (
        '所有类型','文本文件', '图片文件', '音频文件', '系统文件', '压缩文件', '视频文件', '可执行文件', '程序源文件', '映像文件', '数据库文件')
        self.f1_Rtype.current(0)
        self.f1_Rtype.pack(side='left')
        self.button2 = Button(f1, text='查找', font=('黑体',10), image=im_2,bd=0, command=self.Find)
        self.button2.pack(side='left')

        # 结果显示区域
        self.f2 = LabelFrame(self.t, text='结果显示', height=370)
        self.f2.pack(pady='10',fill="both",expand=YES)
        self.f2.pack_propagate(0)
        self.tree = ttk.Treeview(self.f2, show='headings', height=100, selectmode='extended')
        mycoll1 = Scrollbar(self.f2, orient=VERTICAL)
        mycoll1.pack(side=RIGHT, fill=Y)
        mycoll1.config(command=self.tree.yview)
        mycoll2 = Scrollbar(self.f2, orient=HORIZONTAL)
        mycoll2.pack(side=BOTTOM, fill=X)
        mycoll2.config(command=self.tree.xview)
        self.tree.config(xscrollcommand=mycoll2.set,yscrollcommand=mycoll1.set)
        self.tree.pack(fill='both',expand=False)
        self.menubar = Menu(self.tree,tearoff=0)
        self.menubar.add_command(label='打开', command=self.Open)
        self.menubar.add_command(label='打开文件路径', command=self.Openfiles)
        self.menubar.add_command(label='移动文件', command=self.Move)
        self.menubar.add_command(label='保存文件', command=self.Copy)
        self.menubar.add_command(label='保存源目录结构', command=self.Copy_tree)
        self.menubar.add_separator()
        self.menubar.add_command(label='删除文件', command=self.Delete)
        self.tree.bind('<Button-3>', self.createMenu)
        self.tree.bind('<Double-1>',self.Double_Click)
        self.tree.bind('<ButtonRelease-1>', self.treeviewClick)
        self.tree.bind('<Control-a>',self.select_all_input)
        # 提示区域
        f4 = Frame(self.t,bg='ivory')
        f4.pack(fill='both')
        Label(f4, textvariable=self.num_Var,anchor=W,bitmap='gray12',text=self.num_Var,compound='left',bg='ivory').pack(side='left')
        self.t.mainloop()

    def Open(self):
        for item in self.tree.selection():
            item_text = self.tree.item(item, "values")
            file = item_text[0]
            filepath = item_text[1]
            file_path = os.path.join(filepath, file)
            if os.path.isfile(file_path):
                subprocess.run('start ' + file_path,shell=True)
            else:
                subprocess.run('start ' + filepath, shell=True)

    def Openfiles(self):
        for item in self.tree.selection():
            item_text = self.tree.item(item, 'values')
            filepath = item_text[1]
            subprocess.run('start ' + filepath, shell=True)
    def Delete(self):
        self.need_filepath.clear()
        list = []
        for item in self.tree.selection():
            list.append(item)
        for items in list:
            item_text = self.tree.item(items, "values")
            file = item_text[0]
            filepath = item_text[1]
            file_path = os.path.join(filepath, file)
            if os.path.exists(file_path):
                os.remove(file_path)
                self.tree.delete(items)
        self.num_Var.set(str(len(self.tree.get_children()))+' 个对象')

    def select_all_input(self,event):      #   'Ctrl+A'全选
        iid = self.tree.identify_row(event.y)
        if iid:
            self.tree.selection_set(iid)
            for item in self.tree.get_children():
                self.tree.selection_add(item)
            self.treeviewClick(event)
    def createMenu(self, event):
        list = []
        for item in self.tree.selection():
            list.append(item)
        iid = self.tree.identify_row(event.y)
        if iid:
            if iid in list:
                self.tree.selection_set(list)
                self.menubar.post(event.x_root, event.y_root)
            else:
                self.tree.selection_set(iid)
                self.menubar.post(event.x_root, event.y_root)
            # mouse pointer over item

    def Find(self):
        if len(self.f1_Rpath.get()) == 0:
            messagebox.showinfo('', '源文件路径不能为空！')
        elif len(self.f1_Rpath.get())!=0 and os.path.exists(self.f1_Rpath.get()) is False:
            messagebox.showinfo('', '源文件路径不正确！')
        else:
            self.Find_file()

    def Find_KeyWord1(self, file):
        Word = self.f1_Rname.get().strip(' ')
        res = re.search(r'' + Word, file)
        return res

    def Filelogue(self):
        drive =self.f1_Rpath.get()
        for a, b, c in os.walk(drive):
            for file in c:
                filename = os.path.join(a, file)
                if os.path.isfile(filename):
                    m,n = os.path.splitext(filename)
                    if n in self.classfication[self.type.get()]:
                        if self.Find_KeyWord1(file) is not None:
                            filename = filename.replace('/', '\\')
                            self.file_name.append(filename)
        self.file_name.sort(key=lambda x: os.path.getmtime(x)) #按时间顺序排序，由小到大
    def Find_file(self):
        def result():
            x = self.tree.get_children()
            for item in x:
                self.tree.delete(item)
            # 定义列
            self.tree["columns"] = ("文件名", "文件路径","修改时间")  # 列名
            # 设置列，列还不显示
            self.tree.column("文件名", minwidth =250, stretch = False)
            self.tree.column("文件路径",minwidth =380   )
            self.tree.column("修改时间", minwidth =170,  stretch = False, anchor='center')
            # 设置表头
            self.tree.heading("文件名", text="文件名")  # 表头显示text
            self.tree.heading("文件路径", text="文件路径")
            self.tree.heading("修改时间", text="修改时间")
            self.tree.column("文件路径")["selectmode"] = "none"
            # 添加数据
            for file in self.file_name:
                self.num_Var.set(str(len(self.file_name))+' 个对象')
                m, n = os.path.split(file)
                c = time.localtime(os.stat(file).st_mtime)
                nowtime = time.strftime('%Y-%m-%d %H:%M:%S', c)
                self.tree.insert('','end', value=(n, m, nowtime))
                if m not in self.path_find:
                    self.path_find.append(m)
            for col in ("文件名", "文件路径","修改时间"):  # 绑定函数，使表头可排序
                self.tree.heading(col, text=col, command=lambda _col=col: self.treeview_sort_column(self.tree, _col, False))
        self.file_name.clear()
        self.path_find.clear()
        self.Filelogue()
        result()

    def treeview_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.treeview_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

    def Copy_tree(self):
        path = tkinter.filedialog.askdirectory(title='保存到')
        if os.path.isdir(path):
            fp = {}
            src = self.f1_Rpath.get()
            for dn, dns, fns in os.walk(src):
                for fl in fns:
                    m, n = os.path.splitext(fl)
                    if n in self.classfication[self.type.get()]:
                        if self.Find_KeyWord1(fl) is not None:
                            if dn not in fp.keys():
                                fp[dn] = []
                            fp[dn].append(fl)
            for k, v in fp.items():
                relativepath = k[len(src) + 1:]
                newpath = os.path.join(path, relativepath)
                for f in v:
                    oldfile = os.path.join(k, f)
                    oldfile = oldfile.replace('/', '\\')
                    if oldfile in self.need_filepath:
                        if not os.path.exists(newpath):
                            os.makedirs(newpath)
                        shutil.copy(oldfile, newpath)

    def Copy(self):
        path = tkinter.filedialog.askdirectory(title='保存到')
        if os.path.isdir(path):
            for old in self.need_filepath:
                shutil.copy(old, path)
    def Move(self):
        path = tkinter.filedialog.askdirectory(title='移动到')
        if os.path.isdir(path):
            self.need_filepath.clear()
            list = []
            for item in self.tree.selection():
                list.append(item)
            for items in list:
                item_text = self.tree.item(items, "values")
                file = item_text[0]
                filepath = item_text[1]
                file_path = os.path.join(filepath, file)
                if os.path.exists(file_path):
                    shutil.move(file_path, path)
                    path = path.replace('/','\\')
                    if path in self.path_find:
                        self.tree.set(items, column='#2', value=path)
                    else:
                        self.tree.delete(items)
            self.num_Var.set(str(len(self.tree.get_children())) + ' 个对象')

    def Double_Click(self,event):   # 双击
        if self.tree.identify_region(event.x, event.y) == 'cell':
            for item in self.tree.selection():
                item_text = self.tree.item(item, 'values')
                filepath = item_text[1]
                os.system('start ' + filepath)
    def treeviewClick(self,event):  # 单击
        self.need_filepath.clear()
        list = []
        for item in self.tree.selection():
            list.append(item)
        for items in list:
            item_text = self.tree.item(items, "values")
            file = item_text[0]
            filepath = item_text[1]
            file_path = os.path.join(filepath, file)
            if file_path not in self.need_filepath:
                self.need_filepath.append(file_path)

    def Path(self):
        fn = tkinter.filedialog.askdirectory()
        if fn is not None:
            self.path.set(fn)
if __name__ == '__main__':
    start = FileDoing()
# pyinstaller -F -w --icon='11.ico' test.py