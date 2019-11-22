class Animal:
    def shout(self):
        print("动物叫了一声")

class Dog(Animal):
    def shout(self):
        print("小狗，汪汪汪")

class Cat(Animal):
    def shout(self):
        print("小猫，喵喵喵")

def atnimalShou(a):
    if isinstance(a,Animal):
        a.shout()
    else:
        print("不是动物的不能叫")
atnimalShou(Dog())
atnimalShou(Cat())
