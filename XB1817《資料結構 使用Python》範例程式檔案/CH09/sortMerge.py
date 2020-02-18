#合併排序法
def sortMerge(Ary):
   print('分割數列', Ary)
   length = len(Ary) #取得陣列長度
   if length > 1:
      base = length // 2 #取整數商
      leftArray = Ary[:base] #取得數列左半部資料
      rightArray = Ary[base:] #取得數列右半部資料

      sortMerge(leftArray) #針對數列左半部呼叫遞廻
      sortMerge(rightArray) #針對數列右半部呼叫遞廻
      
      sini = ridx = idx = 0 #左、右、陣列的索引
      leftLen = len(leftArray)
      rightLen = len(rightArray)

      while sini < leftLen and ridx < rightLen:
         if leftArray[sini] < rightArray[ridx]:   #左半部小於右半部
            Ary[idx] = leftArray[sini] #左半部小值設給陣列
            sini += 1
         else:
            Ary[idx] = rightArray[ridx] #右半部若比較小就賦予陣列
            ridx += 1
         idx += 1 #陣列的索引加1
      #print()

      while sini < leftLen: #左半部的長度小於陣列
         Ary[idx] = leftArray[sini]
         sini += 1; idx += 1
      
      while ridx < rightLen: #右半部的長度小於陣列
         Ary[idx] = rightArray[ridx]
         ridx += 1; idx += 1
   #print('合併數列', Ary)

source = [197, 226, 514, 413, 128, 372, 311, 645, 270]
sortMerge(source)
print(source)

