#第10章 實作題二 - 非遞廻的二元搜尋法
def searchBinaryNon(Ary, key): # Iterative
   high, low = len(Ary), 0
   while low < high :
      mid = (high + low)//2
      if key == Ary[mid] : 
         return mid
      elif key < Ary[mid]: 
         high = mid
      else : 
         low = mid + 1
   return None

data = [117, 325, 513, 139, 89, 163, 749, 41, 213, 833]
sortedData = sorted(data)
print('已排序', sortedData)
target = 325
print('Index:', searchBinaryNon(sortedData, target))