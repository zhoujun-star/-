#_*_coding:utf-8_*_
class User(object):
    def __init__(self,name,password):
        self.name=name
        self.password=password

root=User("root","123456")
order = input("1:注册,2:登录(退出exit)")
userInfo = {"root":root}
while order.upper()!="EXIT":
    if order == "1":
        name = input("请输入用户名：")
        password=input("请输入密码：")
        if name.strip() == " ":
            print("输入有误")
        elif name in userInfo:
            print("该用户已存在，注册失败")
        else:
            temp=User(name,password)
            userInfo[name]=temp
            print("注册成功")
    elif order =="2":#登录
        name =input("请输入用户名：")
        password=input("请输入密码：")
        if name in userInfo:
            if password == userInfo.get(name).password:
                print("登录成功")
            else:
                print("密码错误")
        else:
            print("用户名不存在")
    else:
        print("操作错误")
    order = input("1:注册,2:登录(退出exit)")
if order=="exit":
    print("退出")
