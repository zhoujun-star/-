#######################################################
#文件名：ex060301(6.3.1 深度优先遍历 算法6-12~算法6-13 6.3.2 广度优先遍历 算法6-14)
#版本号：0.3
#创建时间：2017-12-10
#修改时间：2017-12-16
#######################################################
#######################################################
#类名称：CircularSequenceQueue
#类说明：定义一个循环队列
#类释义：提供循环顺序队列的相关操作
##############################################################
class CircularSequenceQueue(object):
    ############################
    #默认的初始化循环队列的函数
    ############################
    def __init__(self):
        self.MaxQueueSize=10
        self.s=[None for x in range(0,self.MaxQueueSize)]
        self.front=0
        self.rear=0
    #############################
    #判断循环队列是否为空的函数
    #############################
    def IsEmptyQueue(self):
        if self.front==self.rear:
             iQueue=True
        else:
             iQueue=False
        return iQueue
    #############################
    #元素入队的函数
    #############################
    def EnQueue(self,x):
          if (self.rear+1)%self.MaxQueueSize!=self.front:
              self.rear=(self.rear+1)%self.MaxQueueSize
              self.s[self.rear]=x
          else:
            return
    #############################
    #元素出队的函数
    #############################
    def DeQueue(self):
        if self.IsEmptyQueue():
           return
        else:
            self.front=(self.front+1)%self.MaxQueueSize
            return self.s[self.front]
    #############################
    #获取当前队首元素的函数
    #############################
    def GetHead(self):
        if self.IsEmptyQueue():
            return
        else:
            return self.s[(self.front+1)%self.MaxQueueSize]
#类名称：Vertex
#类说明：定义图中的一个顶点
#类释义：有数据data、与该顶点相关联的第一条边FirstArc
#######################################################
class Vertex(object):
    def __init__(self,data):
        self.data = data
        self.FirstArc = None
##########################################################
#类名称：Acr
#类说明：定义图中的一条边
#类释义：包含该边的一个顶点adjacent、与该边相关的信息info和
#        与该边依附于相同顶点的另一条边NextArc
##########################################################
class Arc(object):
    def __init__(self,adjacent):
        self.adjacent = adjacent
        self.info = None
        self.NextArc = None
##################################################################
#类名称：Graph
#类说明：定义一个图
#类释义：包含该图的类型kind(0无向图，1无向网，2有向图，3有向网)、
#        图中的顶点数VertexNum、边或弧的数目ArcNum和邻接表Vertices
##################################################################
class Graph(object):
    def __init__(self,kind):
        self.kind = kind
        self.VertexNum = 0
        self.ArcNum = 0
        self.Vertices = []
    #############################################
    #以邻接表作为存储结构创建有向图或无向图的方法
    #############################################
    def CreateGraph(self):
        #依次输入顶点的值，创建顺序存储结构
        print('请依次输入图中各顶点的值，每个顶点值以回车间隔，并以#作为输入结束符：')
        data = input('->')
        while data is not '#':
            vertex = Vertex(data)
            self.Vertices.append(vertex)
            self.VertexNum = self.VertexNum + 1
            data = input('->')
        #依次输入边或弧的两个顶点，并进行定位
        print('请依次输入图中每条边的两个顶点值，两个顶点值以空格作为间隔，每输入一组后进行换行，最终以#结束输入：')
        arc = input('->')
        while arc is not '#':
            TailVertex = arc.split()[0]
            HeadVertex = arc.split()[1]
            TailIndex = self.LocateVertex(TailVertex)
            HeadIndex = self.LocateVertex(HeadVertex)
            #将与输入的两个顶点相关联的边插入到顶点的链表当中
            self.InsertArc(TailIndex, HeadIndex)
            self.ArcNum = self.ArcNum + 1
            arc = input('->')
        #创建成功
        print('创建成功!')
    ##################################
    #定位顶点在邻接表中的位置的方法
    ##################################
    def LocateVertex(self,Vertex):
        index = 0
        while self.Vertices[index].data != Vertex and index < len(self.Vertices):
            index = index + 1
        return index
    ##################################
    #将图中的边或弧插入邻接表的方法
    ##################################
    def InsertArc(self,TailIndex,HeadIndex):
        if self.kind is 0:#无向图
            TailArc = Arc(TailIndex)
            HeadArc = Arc(HeadIndex)
            #对TailVertex，插入HeadVertex
            HeadArc.NextArc = self.Vertices[TailIndex].FirstArc
            self.Vertices[TailIndex].FirstArc = HeadArc
            #对HeadVertex，插入TailVertex
            TailArc.NextArc = self.Vertices[HeadIndex].FirstArc
            self.Vertices[HeadIndex].FirstArc = TailArc
        elif self.kind is 2:#有向图
            #对TailVertex，插入HeadVertex
            HeadArc = Arc(HeadIndex)
            HeadArc.NextArc = self.Vertices[TailIndex].FirstArc
            self.Vertices[TailIndex].FirstArc = HeadArc
    ##################################
    #得到某一顶点的第一个邻接点的方法
    ##################################
    def GetFirstAdjacentVertex(self,Vertex):
        FirstArc = self.Vertices[Vertex].FirstArc
        if FirstArc is not None:
            return FirstArc.adjacent
    #################################################
    #得到某一顶点相对于Adjacent的下一个邻接点的方法
    #################################################
    def GetNextAdjacentVertex(self,Vertex,Adjacent):
        ArcLink = self.Vertices[Vertex].FirstArc
        while ArcLink is not None:
            if ArcLink.adjacent is Adjacent:
                if ArcLink.NextArc is not None:
                    return ArcLink.NextArc.adjacent
                else:
                    return None
            else:
                ArcLink = ArcLink.NextArc
    '''深度遍历'''
    def DFSTraverse(self):
        visited = []
        index = 0
        while index < self.VertexNum:
            visited.append('False')
            index = index + 1
        index = 0
        while index < self.VertexNum:
            if visited[index] is 'False':
                self.DFS(visited, index)
            index = index + 1

    def DFS(self, visited, Vertex):
        visited[Vertex] = 'True'
        self.VisititVertex(Vertex)
        NextAdjacent = self.GetFirstAdjacentVertex(Vertex)
        while NextAdjacent is not None:
            if visited[NextAdjacent] is 'False':
                self.DFS(visited, NextAdjacent)
            NextAdjacent = self.GetNextAdjacentVertex(Vertex, NextAdjacent)
    '''广义遍历'''
    def BFSTraverse(self):
        visited = []
        index = 0
        Queue = CircularSequenceQueue()
        while index<self.VertexNum:
            visited.append('False')
            index=index+1
        index=0
        while index < self.VertexNum:
            if visited[index] is 'False':
                visited[index]='True'
                self.VisititVertex(index)
                Queue.EnQueue(index)
                while Queue.IsEmptyQueue() is False:
                    tVertex=Queue.DeQueue()
                    NextAdjacent=self.GetFirstAdjacentVertex(tVertex)
                    while NextAdjacent is not None:
                        if visited[NextAdjacent] is 'False':
                            visited[NextAdjacent]='True'
                            self.VisititVertex(NextAdjacent)
                            Queue.EnQueue(NextAdjacent)
                        NextAdjacent=self.GetNextAdjacentVertex(tVertex,NextAdjacent)
            index+=1
    '''判断是否连通'''
    def IsConnect(self):
        visited = []
        index = 0
        while index < self.VertexNum:
            visited.append('False')
            index = index + 1
        visit=[]
        for i in self.Vertices:
            visit.append(i)
        Queue = CircularSequenceQueue()
        Queue.EnQueue(0)
        while Queue.IsEmptyQueue() is False:
            tVertex=Queue.DeQueue()
            NextAdjacent = self.GetFirstAdjacentVertex(tVertex)
            while NextAdjacent is not None:
                if visited[NextAdjacent] is 'False':
                    visited[NextAdjacent] = 'True'
                    visit.remove(self.Vertices[NextAdjacent])
                    Queue.EnQueue(NextAdjacent)
                NextAdjacent = self.GetNextAdjacentVertex(tVertex, NextAdjacent)
        if len(visit)==0:
            print('该无向网：连通')
        else:
            print('该无向网：不连通')

    def VisititVertex(self, Vertex):
        print(self.Vertices[Vertex].data, end=' ')

###############
#主程序
###############
if __name__ =='__main__':
    #创建有向图
    graph = Graph(0)
    graph.CreateGraph()
    #深度优先递归遍历图
    print('深度优先递归遍历图的结果如下:')
    graph.DFSTraverse()
    print()
    #广度优先遍历图
    print('广度优先遍历图的结果如下:')
    graph.BFSTraverse()
    print()
    graph.IsConnect()
