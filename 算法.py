#_*_coding:utf-8_*_
def func():
    ls = []
    ls.append(1)
    return ls
a = func()
b = func()
print(a,b)
print(id(a))
print(id(b))

def func(ls = []):
    ls.append(1)
    return ls
a = func()
b = func()
print(a,b)
print(id(a))
print(id(b))

if __name__ == "__main__":
    a=[1]
    b=a
    a.append("hha")
    print(b)
    print(id(a))
    print(id(b))