class Diction(object):
    def __init__(self):
        self.dict = {}

    def MathTeam(self):
        stringSH = input('输入：')
        for i in stringSH:
            self.dict[i] = self.dict.get(i, 0) + 1
        ls=list(self.dict.items())
        ls.sort(key=lambda x:x[1],reverse=True)
        print(ls)


SH = Diction()
SH.MathTeam()
