class SequenceQueue(object):
    def __init__(self, Max):
        self.front = 0
        self.rear = 0
        self.MaxQueueSize = Max
        self.s = [None for x in range(0, self.MaxQueueSize)]

    def IsEmptyQueue(self):
        if self.front == self.rear:
            iTop = True
        else:
            iTop = False
        return iTop

    def QueueTravers(self):
        if self.IsEmptyQueue():
            print('当前队列已空!')
        else:
            for i in range(self.front+1, self.rear+1):
                print(self.s[i], end='  ')
            print(' ')
        return

    def EnQueue(self, x):
        if self.rear < self.MaxQueueSize - 1:
            self.rear = self.rear + 1
            self.s[self.rear] = x
            print('当前进队元素为:', x)
        else:
            print('当前队列满!')

    def CreateQueueByInput(self):
        da = input('请输入元素("#"结束):')
        while da != '#':
            self.EnQueue(da)
            da = input('请输入元素("#"结束):')

    def GetHead(self):
        if self.IsEmptyQueue():
            print('队列为空,无法输出对头元素')
            return
        else:
            return self.s[self.front]

    def GetQueueLength(self):
        length = self.rear - self.front
        print('当前队列元素长度为：', length)

    def DeQueue(self):
        if self.IsEmptyQueue():
            print('队列为空，无法出队')
        else:
            self.front = self.front + 1
            print('当前出队元素为：',self.s[self.front])
            return self.s[self.front]


ls = SequenceQueue(10)
ls.IsEmptyQueue()
ls.QueueTravers()
ls.CreateQueueByInput()
ls.GetHead()
ls.GetQueueLength()
ls.DeQueue()
ls.QueueTravers()
ls.EnQueue(input('输入一个新元素:'))
