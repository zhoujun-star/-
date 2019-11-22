# _*_coding:utf-8_*
class StringList(object):
    def __init__(self):
        self.MaxStringSize = 256
        self.chars = ''
        self.length = 0

    def IsEmpty(self):
        if self.length == 0:
            return True
        else:
            return False

    def CreateString(self):
        stringSH = input('请输入字符串,按回车键结束输入：')
        if len(stringSH) > self.MaxStringSize:
            print('当前字符序列长度超过分配的存储空间,超过的部分无法存入当前串。')
            self.chars = stringSH[:self.MaxStringSize]
        else:
            self.chars = stringSH
        self.length = len(self.chars)

    def StringConcat(self, strSrc):
        lengthSrc = strSrc.length
        stringSrc = strSrc.chars
        if len(self.chars) + lengthSrc <= self.MaxStringSize:
            self.chars = self.chars + stringSrc
        else:
            print('两个字符串连接后超过分配的存储空间，超过部分无法存入当前串')
            size = self.MaxStringSize - len(self.chars)
            self.chars = self.chars + stringSrc[0:size]
        self.length = len(self.chars)
        print('连接后的字符串为：', self.chars)

    def SubString(self, iPos, length):
        if iPos > len(self.chars) - 1 or iPos < 1 or iPos + length > len(self.chars):
            print('无法获取字串。')
        else:
            substr = self.chars[iPos:iPos + length]
            print('获取的字串为：', substr)

    def StringCopy(self, strSrc):
        self.chars = strSrc.chars
        self.length = len(self.chars)
        print('复制后当前顺序串为：',self.chars)

    def StringCompare(self, strSrc):
        if strSrc.length > self.length:
            a = strSrc.length
        else:
            a = self.length
        if strSrc.chars==self.chars:
            print('两个顺序串相等都为：',strSrc.chars)
        else:
            for i in range(a):
                if strSrc.chars[i] == self.chars[i]:
                    continue
                elif strSrc.chars[i] > self.chars[i]:
                    print('当前字符串序列较大的为：', strSrc.chars)
                    break
                else:
                    print('当前字符串序列较大的为：', self.chars)
                    break

    def StringDelete(self, iPos, length):
        if iPos > len(self.chars) - 1 or iPos < 0 or iPos + length > len(self.chars) or length < 1:
            print('无法删除字符')
        else:
            self.chars = self.chars[:iPos] + self.chars[iPos + length - 1:]
            self.length = len(self.chars)
            print('删除字串后为：', self.chars)

    def StringInsert(self, iPos, strSrc):
        if iPos > len(self.chars) - 1 or iPos < 0:
            print('输入位置有误！')
        else:
            new1 = self.chars[:iPos]
            new2 = self.chars[iPos:]
            self.chars = new1 + strSrc.chars + new2
            print('插入串strSrc后为：', self.chars)


StringSrc = StringList()
StringSrc.CreateString()             #创建顺序串StringSrc

StringDst = StringList()
StringDst.CreateString()             #创建顺序串StringDst
StringDst.StringCopy(StringSrc)      #复制
StringDst.StringCompare(StringSrc)   #比较
StringDst.StringConcat(StringSrc)    #连接
StringDst.SubString(1,3)             #获取
StringDst.StringDelete(2,4)          #删除
StringDst.StringInsert(2,StringSrc)  #插入