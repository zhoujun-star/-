# -*- coding: utf-8 -*-
class User(object):
    def __init__(self,name,password):
        self.name=name
        self.password=password
    def Get(self):
        return self.name
order=input("(1)注册/(2)登陆/(EXIT)退出")
temp=User("root","123")
userInfor={"root":temp}
while order.upper() != "EXIT":
    if order =="1":
        name=input("")
        password=input("")
        if name.strip()=="":
            print("输入错误")
        elif name in userInfor:
            print("该用户存在")
        else:
            temp1=User(name,password)
            userInfor[name]=temp1
            print("注册成功")
    elif order =="2":
        name = input("")
        password = input("")
        if name in userInfor:
            if password == userInfor.get(name).password:
                print("登陆成功")
            else:
                print("密码错误")
        else:
            print("该用户不存在")
    elif order =="3":
        name=input("")
        if name in userInfor:
            password=input("")
            if password == userInfor.get(name).password:
                Newpassword=input("")
                temp2=(name,Newpassword)
                User[name]=temp2
                print("修改成功")
            else:
                print("密码错误")
        else:
            print("该用户不存在")
    else:
        print("操作错误")
    order = input("(1)注册/(2)登陆/(EXIT)退出")
if order.upper()=="EXIT":
    print("退出成功")
