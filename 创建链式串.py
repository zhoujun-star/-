# _*_coding:utf-8_*_

class StringNode(object):
    def __init__(self):
        self.data = None
        self.next = None


class StringList(object):
    def __init__(self):
        self.head = StringNode()
        self.tail = self.head
        self.lenght = 0

    def CreateString(self):
        stringSH = input('请输入字符串，按回车结束输入：\n')
        while self.lenght < len(stringSH):
            Tstring = StringNode()
            Tstring.data = stringSH[self.lenght]
            self.tail.next = Tstring
            self.tail = Tstring
            self.lenght += 1

    def StringCopy(self, strSrc):
        self.head = strSrc.head
        self.tail = strSrc.tail
        self.lenght = strSrc.lenght

    def StringConcat(self, strSrc):
        self.tail.next = strSrc.head
        self.tail = strSrc.tail
        self.lenght = self.lenght + strSrc.length

    def GetString(self):
        temp = ''
        tNode = self.head.next
        while tNode != None:
            temp = temp + tNode.data
            tNode = tNode.next

    def StringCompare(self, strSrc):
        ahead = self.head.next
        bhead = strSrc.head.next
        aSrc = ''
        bDst = ''
        while ahead != None:
            aSrc = aSrc + ahead.data
            ahead = ahead.next
        while bhead != None:
            bDst = bDst + bhead.data
            bhead = bhead.next
        if aSrc > bDst:
            print('当前字符串较大的为：', aSrc)
        elif aSrc < bDst:
            print('当前字符串较大的为：', bDst)
        else:
            print('当前两个字符串相等！')

    def StringDelete(self, iPos, lenght):
        Tstring = self.head
        if 0 < iPos <= self.lenght and self.lenght > 0:
            for m in range(iPos - 1):
                Tstring = Tstring.next
        if iPos + lenght - 1 > self.lenght:
            print('超过长度，超过部分不删除！')
            T1string = Tstring
            for n in range(self.lenght - iPos):
                T1string = T1string.next
            Tstring.next = None
            self.tail = Tstring
        else:
            T1string = Tstring
            for s in range(lenght):
                T1string = T1string.next
            Tstring.next = T1string.next
            T1string.next = None
        str = ''
        tstring = self.head
        while tstring.next != None:
            tstring = tstring.next
            str = str + tstring.data

        print('删除子串后字符串序列为：', str)

    def StringInsert(self, iPos, strSrc):
        T1 = strSrc.head
        T2 = self.head
        if iPos < 0 or iPos > self.lenght or self.lenght == 0:
            print('位置有误！')
        elif iPos == self.lenght:
            self.tail.next = T1.next
            self.tail = T1.tail
        else:
            for i in range(iPos):
                T2 = T2.next
            strSrc.tail.next = T2.next
            T2.next = T1.next
        str = ''
        t = self.head
        while t.next != None:
            t = t.next
            str = str + t.data
        print('插入子串后字符串序列为：', str)


if __name__ == '__main__':
    StringSrc = StringList()
    StringSrc.CreateString()
    StringDst = StringList()
    StringDst.CreateString()
    StringDst.StringCompare(StringSrc)
    StringDst.StringDelete(2, 2)
    StringDst.StringInsert(2, StringSrc)
