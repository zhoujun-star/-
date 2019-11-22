class Matrix(object):
    def __init__(self):
        self.matrix = []
        self.matrix1 = []

    def Matrix(self, a=int(input('请输入行数:')), b=int(input('请输入列数:'))):
        for i in range(a):
            row = []
            for j in range(b):
                a = input('请输入值:')
                row.append(a)
            self.matrix.append(row)
        return self.matrix

    def EachAdd(self, num1):
        for i in range(len(num1)):
            row = []
            for j in range(len(num1[0])):
                a = int(num1[i][j]) + int(self.matrix[i][j])
                row.append(a)
            self.matrix1.append(row)
        return self.matrix1

    def Traval(self, matrix):
        for i in matrix:
            n = 0
            for j in i:
                print(j, end='  ')
                n += 1
                if n == len(matrix[0]):
                    print()


a = Matrix()
s = a.Matrix()
print('生成矩阵为:\n')
a.Traval(s)
b = Matrix()
c = b.Matrix()
print('生成矩阵为:\n')
b.Traval(c)
d = b.EachAdd(s)
print('相加后矩阵为:\n')
b.Traval(d)
