#費氏搜尋法
def searchFibon(target, Ary, num):
   fib = fibNums(len(Ary))
   fk = getPos(fib, num + 1)
   start = num - fib[fk] #設定查找的第一個項目 F(3)=2
   ind = k = fk - 1

   if target >  Ary[ind]:
      ind += start

   while fib[k] > 0:
      #搜尋值 > 目前分割項
      if target > Ary[ind]:
         #費氏數減1級, 向左子樹找
         k -= 1
         ind += fib[k]
         print('Lfib', fib[k], Ary[ind])
      elif target < Ary[ind]:
         #費氏數減1級, 向右子樹找
         k -= 1
         ind -= fib[k]
      else:
         return ind
   return None

def fibNums(num):   #產生費氏級數
   fib = []
   one, two = 0, 1 
   for item in range(num):
      one, two = two, one + two 
      fib.append(one)
   return fib

def getPos(fib, num): #取得費氏級數的位置
   item = 0
   while fib[item] <= num:
      item += 1
   return item - 1 #F(k - 1), F(5) = 8, 為費氏樹根節點

store = [152, 54, 49, 118, 141, 74, 186, 432, 69, 163, 130]
num = len(store) - 1
newData = sorted(store)
print(newData)
print('Index:', searchFibon(141, newData, num))