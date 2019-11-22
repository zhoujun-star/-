# _*_coding:utf-8_*_
class StackNode(object):
    def __init__(self):
        self.data = None
        self.next = None


class LinkStack(object):
    def __init__(self):
        self.top = StackNode()

    def PushStack(self, da):
        tStackNode = StackNode()
        tStackNode.data = da
        tStackNode.next = self.top.next
        self.top.next = tStackNode
        print('当前进栈元素为：', da)

    def IsEmpty(self):
        if self.top.next is None:
            iPos = True
        else:
            iPos = False
        return iPos

    def CreatStack(self):
        data = input('输入元素(以"#"结束)：')
        while data != '#':
            self.PushStack(data)
            data = input('输入元素(以"#"结束)：')

    def GetTopStack(self):
        if self.IsEmpty():
            print('栈空')
            return
        else:
            print('当前栈顶元素为:', self.top.next.data)
            return self.top.next.data

    def TravalStack(self):
        if self.IsEmpty():
            print('栈空')
        else:
            iTop = self.top
            while iTop.next is not None:
                iTop = iTop.next
                print(iTop.data, end=' ')
            print(' ')

    def PopStack(self):
        if self.IsEmpty():
            print('栈空')
            return
        else:
            tStackNode = self.top.next
            self.top.next = tStackNode.next
            tStackNode.next = None
            return tStackNode.data

    def ByPopStack(self):
        if self.IsEmpty():
            return
        else:
            while self.top.next is not None:
                print('当前出栈元素为:', self.PopStack())


S = LinkStack()
S.CreatStack()
S.GetTopStack()
S.TravalStack()
S.ByPopStack()
