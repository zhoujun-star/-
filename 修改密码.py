# _*_ coding:utf-8 _*_
class ID:
    def __init__(self,haoma,mima):
        self.haoma=haoma
        self.mima=mima
root = ID('haoma','mima')
A=input('1:zhuce,2:denglu,3:gaimima(exit)')
xinxi={'root':root}
while A.upper()!='EXIT':
    if A=='1':
        haoma = input('haoma:')
        mima  =input ('mima:')
        if haoma in xinxi:
            print('you le')
        else:
            temp = ID(haoma,mima)
            xinxi[haoma]=temp
            print('ok')
    elif A=='2':
        haoma = input('haoma:')
        mima = input('mima:')
        if haoma in xinxi:
            if mima == xinxi.get(haoma).mima:
                print('OK')
            else:
                print('mima cuo le')
        else:
            print('haoma cuo le')
    elif A=='3':
        haoma = input('haoma:')
        mima = input('mima:')
        if haoma in xinxi:
            if mima == xinxi.get(haoma).mima:
                newmima=input('new:')
                temp=ID(haoma,newmima)
                xinxi[haoma]=temp
                print('OK')
            else:
                print('mima cuo le')
        else:
            print('haoma cuo le')


    A = input('1:zhuce,2:denglu,3:gaimima(exit)')