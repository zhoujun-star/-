class QueueNode(object):
    def __init__(self):
        self.data=None
        self.next=None
class LinkQueue(object):
    def __init__(self):
        tQueueNode=QueueNode()
        self.front=tQueueNode
        self.rear=tQueueNode
    def IsEmptyQueue(self):
        if self.front==self.rear:
            iTop=True
        else:
            iTop=False
        return iTop
    def EnQueue(self,da):
        tQueueNode=QueueNode()
        tQueueNode.data=da
        self.rear.next=tQueueNode
        self.rear=tQueueNode
        print('当前进队元素为:',da)
    def CreateQueueByInput(self):
        data=input('请输入元素("#"结束):')
        while data!='#':
            self.EnQueue(data)
            data=input('请输入元素("#"结束):')
    def QueueTraverse(self):
        if self.rear==self.front:
            print('当前队列空!')
        else:
            ifront=self.front
            while ifront.next!=None:
                ifront=ifront.next
                print(ifront.data,end=' ')
            print(' ')

    def GetHead(self):
        if self.IsEmptyQueue():
            print('队列为空')
            return
        else:
            return self.front.next.data
    def GetQueueLength(self):
        if self.IsEmptyQueue():
            print('队列为空')
            return
        else:
            count=0
            iTop=self.front
            while iTop.next!=None:
                iTop=iTop.next
                count=count+1
            print('当前队列元素长度为:',count)
    def DeQueue(self):
        if self.IsEmptyQueue():
            return
        else:
            while True:
                tQueueNode=self.front.next
                self.front.next=tQueueNode
                tQueueNode.next=None

                if self.rear==tQueueNode:
                    self.rear=self.front
                    print('当前出队元素为:',tQueueNode.data)
                    break
            return

ls=LinkQueue()
ls.IsEmptyQueue()
ls.CreateQueueByInput()
ls.QueueTraverse()
# ls.GetHead()
# ls.GetQueueLength()
ls.DeQueue()