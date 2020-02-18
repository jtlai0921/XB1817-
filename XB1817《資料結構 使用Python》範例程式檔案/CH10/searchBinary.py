def searchBinary(target, Ary, low, high):
   mid = (low + high) // 2
   #取出的中間項等於欲搜尋Key，表示找到了
   print('low {}, moddle {}, high {}'.format(low, mid, high))
   if target == Ary[mid]:
      return mid
   #搜尋的值小於中間項，向右邊移動
   elif target < Ary[mid]:
      return searchBinary(target, Ary, low, mid - 1) 
   else:   #搜尋的值大於中間項，向左邊移動
      return searchBinary(target, Ary, mid + 1, high)
   

number = [157, 5, 13, 118, 89, 123, 18, 101, 56, 21, 35]
length = len(number) - 1
sortedItem = sorted(number)   #呼叫sorted()函式做遞增排序
print(sortedItem)
print('索引值：', searchBinary(101, sortedItem, 0, length))