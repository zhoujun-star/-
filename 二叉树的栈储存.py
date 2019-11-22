#非递归先序遍历二叉树
#####定义二叉树的结点
class BinaryTreeNode(object):
    def __init__(self):
        self.data = '#'
        self.LeftChild = None
        self.RightChild = None
#定义二叉树
class BinaryTree(object):
    def CreateBinaryTree(self, Root):
        data = input('->')
        if data == '#':
            Root = None
        else:
            Root.data = data
            Root.LeftChild = BinaryTreeNode()
            self.CreateBinaryTree(Root.LeftChild)
            Root.RightChild = BinaryTreeNode()
            self.CreateBinaryTree(Root.RightChild)
    #def PreOrder(self, Root):
        #if Root is not None:
            #if Root.data is not '#':
                #print(Root.data)
            #self.PreOrder(Root.LeftChild)
            #self.PreOrder(Root.RightChild)

    def front_stack(self, root):
        myStack=SequenceStack()
        TreeNode=root
        myStack.PushStack(TreeNode)
        while myStack.GetStackLength()!=-1:
            TreeNode =myStack.PopStack()
            if TreeNode.data is not '#':
                print(TreeNode.data, end='->')
            if TreeNode.RightChild is not None:
                myStack.PushStack(TreeNode.RightChild)
            if TreeNode.LeftChild is not None:
                myStack.PushStack(TreeNode.LeftChild)

class SequenceStack():
    def __init__(self):
        self.MaxStackSize=10
        self.s=[None for x in range(0, self.MaxStackSize)]
        self.top=-1

    def IsEmptyStack(self):
        if self.top==-1:
              iTop=True
        else:
              iTop=False
        return   iTop

    def PushStack(self, x):

        if self.top<self.MaxStackSize-1:
            self.top=self.top+1
            self.s[self.top]=x
        else:
            print("栈满")
            return

    def PopStack(self):#元素出栈
        if self.IsEmptyStack():
            print("栈为空")
            return
        else:
            iTop=self.top
            self.top=self.top-1
            return self.s[iTop]

    def StackTraverse(self):#依次访问其中元素
        if self.IsEmptyStack():
            print("栈为空")
            return
        else:
            for i in range(0,self.top+1):
                print(self.s[i],end='  ')

    def GetTopStack(self):
        if self.IsEmptyStack():
            print("栈为空")
            return
        else:
            return self.s[self.top]

    def GetStackLength(self):
        if self.top != -1:
            return self.top+1
        else:
            return -1

    def CreatStack(self):
        data = input('输入元素(以"#"结束)：')
        while data != '#':
            self.PushStack(data)
            data = input('输入元素(以"#"结束)：')

if __name__ == '__main__':
    btn = BinaryTreeNode()
    bt = BinaryTree()
    bt.CreateBinaryTree(btn)
    bt.front_stack(btn)

    # def middle_stack(self,root):
    #     if root==None:
    #         return
    #     myStack=[]
    #     node=root
    #     while node or myStack:
    #         while node:
    #             myStack.append(node)
    #             node=node.LeftChild
    #         node=myStack.pop()
    #         print(node.data)
    #         node=node.RightChild
    # def later_stack(self,root):
    #     if root==None:
    #         return
    #     myStack1=[]
    #     myStack2=[]
    #     node=root
    #     myStack1.append(node)
    #     while myStack1:
    #         node=myStack1.pop()
    #         if node.LeftChild:
    #             myStack1.append(node.LeftChild)
    #         if node.RightChild:
    #             myStack1.append(node.RightChild)
    #         myStack2.append(node)
    #     while myStack2:
    #         print(myStack2.pop().data)
    #
    #
    # #def VisitBinaryTreeNode(self,BinaryTreeNode):
    #     #if BinaryTreeNode.data is not "#":
    #         #print(BinaryTreeNode.data)


