# _*_coding:utf-8_*_
class SequenceStack(object):
    def __init__(self):
        self.MaxStackSize = 10
        self.s = [None for i in range(0, self.MaxStackSize)]
        self.top = -1

    def IsEmpty(self):
        if self.top == -1:
            iTop = True
            print('空栈')
        else:
            iTop = False
        return iTop

    def GetTopStack(self):
        if self.IsEmpty():
            print('栈为空。')
            return
        else:
            print('当前栈顶元素为:', self.s[self.top])
            return self.s[self.top]

    def PushStack(self, x):
        if self.top < self.MaxStackSize - 1:
            self.top = self.top + 1
            self.s[self.top] = x
        else:
            print('当前栈满。')
            return

    def CreatStack(self):
        da = input('输入元素(以"#"结束)：')
        while da != '#':
            self.PushStack(da)
            da = input('输入元素(以"#"结束)：')

    def TravalStack(self):
        if self.IsEmpty():
            return
        else:
            for i in range(0, self.top + 1):
                print('栈内元素为：',self.s[i], end='--')
            print(None)

    def GetLength(self):
        if self.top != -1:
            print('当前栈长度为：', self.top + 1)
            return self.top+1
        else:
            return -1

    def PopStack(self):
        if self.IsEmpty():
            return
        else:
            iTop = self.top
            self.top = self.top - 1
            print('当前出栈元素为:', self.s[iTop])
            return self.s[iTop]

    def ByPopStack(self):
        while self.top != -1:
            self.PopStack()


SLL = SequenceStack()
SLL.CreatStack()
SLL.GetTopStack()
SLL.GetLength()
SLL.TravalStack()
SLL.ByPopStack()
