#_*_coding:utf-8_*_
class Node(object):
    def __init__(self,date):
        self.date=date
        self.next=None

class SingLeLinkedList(object):
    def __init__(self):
        self.head=Node(None)
    def Node(self,date):
        self.date = date
        self.next = None

    def CreateSingleLinkedList(self):
        print("请输入数据（以‘#’结束）")
        cNode=self.head
        Elment=input("输入：")
        while Elment !="#":
            nNode=Node(int(Elment))
            cNode.next=nNode
            cNode=cNode.next
            Elment=input("输入：")

    def GetLength(self):
        cNode=self.head
        length=0
        while cNode.next!=None:
            length=length+1
            cNode=cNode.next
        return length

    def IsEmpty(self):
        if self.GetLength() == 0:
            return True
        else:
            return False

    def InsertElenmentMiddle(self):
        Pos=eval(input("待插入的位置："))
        Element=eval(input("待插入的元素："))
        cNode=self.head
        pNode=self.head
        nNode=Node(Element)
        for i in range(Pos):
            pNode=cNode
            cNode=cNode.next
        pNode.next=nNode
        nNode.next=cNode
        print("在",Pos,"位置的元素：",Element)


    def FindElement(self):
        n=eval(input("请输入想要查找元素的位置："))
        cNode=self.head
        if self.IsEmpty():
            print("该单链表为空")
        for i in range(n):
            cNode=cNode.next
        print("查找结点的元素为：",cNode.date)


    def InsertElenmentInhead(self):
        Element=input("请输入要插入的元素：")
        nNode=Node(int(Element))
        cNode=self.head
        nNode.next=cNode.next
        cNode.next=nNode

    def DeleteElement(self):
        key=eval(input("待删除元素结点的位置："))
        cNode=self.head
        pNode=self.head
        Pos=0
        if key>self.GetLength():
            print("输入超出单链表长度",self.GetLength())
        elif self.IsEmpty():
            print("当前单链表为空")
            return
        else:
            while cNode.next!=None and Pos!=key:
              pNode=cNode
              cNode=cNode.next
              Pos=Pos+1
            if Pos==key:
              pNode.next=cNode.next
              del cNode
              print("成功删除含有元素的",key,"位置的结点")
            else:
              print("当前单链表位置为",key,"无结点")
    def TraverseElement(self):
        cNode=self.head
        if cNode.next==None:
            print("当前单链表为空！")
            return
        print("你当前的单链表为：")
        while cNode!=None:
            cNode=cNode.next
            self.VisitElement(cNode)
    def VisitElement(self,tNode):
        if tNode!=None:
            print(tNode.date,"->",end=" ")
        else:
            print("None")
    def A(self):
        p = self.head.next
        q = p.next
        self.head.next = None
        temp = None
        while p is not None:
            temp = self.head.next
            self.head.next = p
            p.next = temp
            p = q
            if q is None:
                q = None
            else:
                q = q.next

SLL=SingLeLinkedList()
SLL.CreateSingleLinkedList()
SLL.A()
#SLL.InsertElenmentMiddle()
SLL.TraverseElement()








