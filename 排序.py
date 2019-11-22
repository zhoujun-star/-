#_*_coding:utf-8_*_
def sort(ls):
    for i in range(len(ls)-1):
        for j in range(len(ls)-1-i):
            if ls[j]>ls[j+1]:
                ls[j],ls[j+1]=ls[j+1],ls[j]
ls = [1,4,2,5,6,8,3,7]
sort(ls)
print(ls)
def sort(mppx):
    size = len(mppx)
    for lastIndex in range(size):
        for index in range(lastIndex):
            if  mppx[index]>mppx[lastIndex]:
                mppx[index],mppx[lastIndex]=mppx[lastIndex],mppx[index]
ls = [1,5,8,9,4,7,10,6]
sort(ls)
print(ls)