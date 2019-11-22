class Person:
    __School="sadasdas"
    def __init__(self,name,age):
        self.name = name
        self.__age = age

    def say_age(self):
        print(self.name,"的年龄是：",self.__age)

class Student(Person):
    pass

s1 = Student("王珺玲",18)
print(s1._Person__School)          #方法：访问类属性里面的内容
#print(dir(s1))
#print(mor(s1))