# 测 试 私 有 属 性 、 私 有 方 法
class Student:
    __school = "重庆第二师范学院"  # 私 有 类 属 性.

    def __init__(self,name,age):
        self.name = name
        self.__age = age  # 私 有 实 例 属 性

    def say_school(self):
        print("我的学校是：",Student.__school)
        print(self.name,"的年龄是：",self.__age)
        self.__work()

    def __work(self):
        print("好好学习，天天向上，毕业找个好工作！")

p1 = Student("weixi",18)
print(p1.name)
p1.say_school()
p1._Student__work()
print(p1._Student__age)
print(dir(p1))
print(p1.__dict__)
