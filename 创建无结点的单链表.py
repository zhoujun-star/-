class Node(object):
    def __init__(self,date):
        self.date=date
        self.next=None
class CreatList(object):
    def Creat(self):
        self.head=Node(date=int(input('请输入头结点值：')))
        cNode=self.head
        Element=input('输入：（以"#"结束）')
        while Element != '#':
            nNode = Node(int(Element))
            cNode.next=nNode
            cNode=cNode.next
            Element=input('输入：（以"#"结束）')
    def InsertElement(self):
        Pos=eval(input('输入结点插入位置：'))
        Element=eval(input('输入插入结点的值：(以"#"结束)'))
        nNode=Node(Element)
        cNode=self.head
        pNode=self.head
        while Element!='#':
            for i in range(Pos-1):
                pNode=cNode
                cNode=cNode.next
            pNode.next=nNode
            nNode.next=cNode
            print('成功在',Pos,'位置插入',Element,'元素')
    def DeleteElement(self):
        Element=eval(input('待删除结点元素：(以"#"结束)'))
        nNode=Node(Element)
        cNode=self.head
        pNode=self.head
        while cNode.next!=None and cNode.date !=nNode.date:
            pNode=cNode
            cNode=cNode.next
        if cNode.date == nNode.date:
            if cNode.date == self.head.date:
                c = self.head
                self.head=self.head.next
                del c
                print('结点元素的值为', Element, '已删除')
            else:
                pNode.next=cNode.next
                del cNode
                print('结点元素的值为',Element,'已删除')
        else:
            print('当前单链表无该结点的值！')

    def VisitElement(self):
        cNode=self.head
        while cNode!=None:
            print(cNode.date,end='->')
            cNode=cNode.next
        if cNode == None:
            print('None')


L=CreatList()
L.Creat()

L.DeleteElement()
L.VisitElement()
