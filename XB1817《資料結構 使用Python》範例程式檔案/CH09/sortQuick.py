#快速排序法
def sortQuick(Ary, first = 0, last = None):
   if last == None: #初值為None，設hing = len(Ary)
      last = len(Ary) - 1 #設hign, index的值
   if first < last:
      pivotIndex = Division(Ary, first, last) #呼叫分割函式
      sortQuick(Ary, first, pivotIndex - 1)#呼叫遞廻，處理左邊的元素
      sortQuick(Ary, pivotIndex + 1, last) #呼叫遞廻，處理右邊的元素      
   return Ary

def Division(Ary, first, last): #將陣列分割
   index = first #取得向右移動的索引
   pivot = Ary[first]#設List第一個元素為pivot
   
   for k in range(first + 1, last + 1):
      
      #if Ary[k] >= pivot: #遞減排序
      #增遞排序
      #if Ary[k] <= pivot: #與pivot做比較，若小於pivot
         index += 1
         #將目前的值與pivot做對調
         Ary[k], Ary[index] = Ary[index], Ary[k]
   left = Ary[first] #最後pivot的值與分割後的第一個值對調
   Ary[first] = Ary[index]
   Ary[index] = left #pivot值與分割後的值對調
   return index

lst = [35, 40, 86, 56, 16, 63, 75, 21]
print('快速排序法', sortQuick(lst))