#_*_coding:utf-8_*_
#1.无循环
print("周俊")
print(1810603126)
#时间复杂度O(1)

#2.单重循环
sum=0
for i in range(0,10):
    sum=sum+i
print(sum)
#时间复杂度O(10)，空间复杂度O(1)

#3.双重循环
for i in range(1,10):
    for j in range(1,10):
        if i>=j:
            print("{0}*{1}={2}".format(i,j,i*j),end=" ")
    print("")
#时间复杂度O(100)，空间复杂度O(1)