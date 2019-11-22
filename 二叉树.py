'''结点类'''
class BinaryTreeNode(object):
    def __init__(self):
        self.data = '#'
        self.left = None
        self.right = None

'''二叉树类'''
class BinaryTree(object):
    def CreateBinary(self, root):
        data=input('->')
        if data == '#':
            root = None
        else:
            root.data=data
            root.left=BinaryTreeNode()
            self.CreateBinary(root.left)
            root.right=BinaryTreeNode()
            self.CreateBinary(root.right)

    def VisitBinaryTreeNode(self, root):
        if root.data is not '#':
            print(root.data,end='->')

    def PreOrder(self, root):
        if root is not None:
            self.VisitBinaryTreeNode(root)
            self.PreOrder(root.left)
            self.PreOrder(root.right)

    def InOrder(self, root):
        if root is not None:
            self.InOrder(root.left)
            self.VisitBinaryTreeNode(root)
            self.InOrder(root.right)

    def PostOrder(self, root):
        if root is not None:
            self.PostOrder(root.left)
            self.PostOrder(root.right)
            self.VisitBinaryTreeNode(root)

    def ChangeNode(self,root,value):
        if root is not None:
            if root.data == value:
                new=input('该子结点的值改变为:')
                root.data=new
                return
            self.ChangeNode(root.left,value)
            self.ChangeNode(root.right,value)

    def AddNewNode(self,root,e,head):
        if root is not None:
            if root.data == e:
                if head==0:
                    if root.left is '#':
                        print('子结点值为', e, '已存在,值为:', root.left.data)
                    else:
                        new = input('该子结点的值为:')
                        root.head.data=new
                        print('添加成功！')
                elif head==1:
                    if root.right is '#':
                        print('子结点值为', e, '已存在,值为:', root.right.data)
                    else:
                        new = input('该子结点的值为:')
                        root.right.data=new
                        print('添加成功！')
            self.AddNewNode(root.left,e,head)
            self.AddNewNode(root.right,e,head)



class CircularSequenceQueue():
    ############################
    # 默认的初始化循环队列的函数
    ############################
    def __init__(self):
        self.MaxQueueSize = 4
        self.s = [None for x in range(0, self.MaxQueueSize)]
        self.front = 0
        self.rear = 0

    ############################
    # 初始化循环队列的函数
    ############################
    def InitQueue(self, Max):
        self.MaxQueueSize = Max
        self.s = [None for x in range(0, self.MaxQueueSize)]
        self.front = 0
        self.rear = 0

    #############################
    # 判断循环队列是否为空的函数
    #############################
    def IsEmptyQueue(self):
        if self.front == self.rear:
            iQueue = True
        else:
            iQueue = False
        return iQueue

    #############################
    # 元素入队的函数
    #############################
    def EnQueue(self, x):
        if (self.rear + 1) % self.MaxQueueSize != self.front:
            self.rear = (self.rear + 1) % self.MaxQueueSize
            self.s[self.rear] = x
        else:
            print("队列已满，无法入队")
            return
            #############################

    # 元素出队的函数
    #############################
    def DeQueue(self):
        if self.IsEmptyQueue():
            print("队列为空，无法出队")
            return
        else:
            self.front = (self.front + 1) % self.MaxQueueSize
            return self.s[self.front]

    def VisitBinaryTreeNode(self, BinaryTreeNode):
        if BinaryTreeNode.data is not '#':
            print(BinaryTreeNode.data,end='->')

    def LevelOrder(self, Root):
        tSequenceQueue = CircularSequenceQueue()
        tSequenceQueue.InitQueue(100)
        tSequenceQueue.EnQueue(Root)
        tTreeNode = None
        while tSequenceQueue.IsEmptyQueue() == False:
            tTreeNode = tSequenceQueue.DeQueue()
            self.VisitBinaryTreeNode(tTreeNode)
            if tTreeNode.left is not None:
                tSequenceQueue.EnQueue(tTreeNode.left)
            if tTreeNode.right is not None:
                tSequenceQueue.EnQueue(tTreeNode.right)

Bin = BinaryTreeNode()
a = BinaryTree()
a.CreateBinary(Bin)
a.PreOrder(Bin)
print()
a.InOrder(Bin)
print()
a.PostOrder(Bin)
print()
a1 = CircularSequenceQueue()
a1.LevelOrder(Bin)
print()
m=input('请输入待修改的子结点值:')
a.ChangeNode(Bin,m)
a.PreOrder(Bin)
print()
e=input('请输入需要添加子结点值:')
a.AddNewNode(Bin, e, 1)
a.PreOrder(Bin)