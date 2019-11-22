#_*_coding:utf-8_*_
class SeqList(object):
    def __init__(self):
        self.seqList=[ ]

    def CreateSeqList(self):
        Element= input("请输入('#'结束):")
        while Element != "#":
            self.seqList.append(int(Element))
            Element= input("请输入('#'结束):")
        if Element == "#":
            print("完成线性表{}的创建".format(self.seqList))
            return self.seqList

    def FindElement(self):
        key=int(input("请输入"))
        if key in self.seqList:
            ipos = self.seqList.index(key)
            print("查找成功!值为",self.seqList[ipos],"的元素,位于当前顺序表的第",ipos+1,"个位置。")
        else:
            print("查找失败！")

    def InsertElement(self):
        ipos=int(input("待添加的元素位置是:"))
        key=input("待添加的元素是:")
        self.seqList.insert(ipos,key)
        print("插入元素后，当前顺序表为：\n",self.seqList)

    def SortSequenList(self):
        key=input("待删除元素是:")
        self.seqList.remove(key)
        print("删除元素后，当前顺序表为：\n",self.seqList)

    def TraverseElement(self):
        i = len(self.seqList)
        for line in range(0,i):
            print("第{}个元素是{}".format(line+1,self.seqList[line]))

    def DestorySequenceList(self):
        self.seqList=None
        print("顺序表销毁成功")

if __name__ == '__main__':

    seqList = SeqList()
    seqList.CreateSeqList()
    seqList.FindElement()
    seqList.InsertElement()
    seqList.TraverseElement()
    seqList.DestorySequenceList()