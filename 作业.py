class SequenceStack(object):
    def __init__(self):
        self.top = -1
        self.MaxStackSize = 10
        self.s = [None for x in range(0, self.MaxStackSize)]

    def IsEmptyStack(self):
        if self.top == -1:
            iTop = True
        else:
            iTop = False
        return iTop

    def PushStack(self, x):
        if self.top < self.MaxStackSize - 1:
            self.top = self.top + 1
            self.s[self.top] = x
        else:
            print('栈满！未成功添加。')

    def PopStack(self):
        if self.IsEmptyStack():
            print('当前栈空！')
        else:
            iTop = self.top
            self.top = self.top - 1
            return self.s[iTop]

    def GetTopStack(self):
        if self.top != -1:
            return self.s[self.top]

    def StackTravers(self):
        if self.IsEmptyStack():
            return
        for i in range(0,self.top+1):
            print(self.s[i],end=' ')

    def BracketMatch(self, str):
        i = 0
        while i < len(str):
            if str[i] == '{':
                ls.PushStack(str[i])
                i = i + 1
            elif str[i] == '}':
                if self.GetTopStack() == '{':
                    ls.PopStack()
                    i = i + 1
                else:
                    ls.PushStack(str[i])
                    i = i + 1
            else:
                i = i + 1
        if ls.IsEmptyStack():
            print('括号配对成功！')
        else:
            print('括号配对不成功！\n未匹配的括号为:')
            ls.StackTravers()


a = '}{{{}'
ls = SequenceStack()
ls.BracketMatch(a)
