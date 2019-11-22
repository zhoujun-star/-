def yueSeFu(listAll,index,step):
   listNew = []
   index = index -1            #下标查找
   size = len(listAll)
   count = 0
   while len(listNew) < size:
        while count<step :
            index = index%size
            curNum = listAll[index]
            if curNum not in listNew:
                count +=1
            index += 1
        listNew.append(curNum)
        count = 0
   return  listNew

ls = [1,2,3,4,5,6,7,8]
print(yueSeFu(ls,3,2))