import random

def searchInterpolation(Ary, target, low, high):
   while low <= high:
      #預測target的落點
      if (Ary[high] - Ary[low]) != 0:
         point = (int)(target - Ary[low]) / \
               (Ary[high] - Ary[low])
      else:
         point = 0

      #依據比例做預測
      middle = low + (int)(point * (high - low))
      #情形一：兩者相等，表示找到key
      if target == Ary[middle]:
         return middle
      #搜尋的值大於中間項，向右邊移動
      if target > Ary[middle]:
         low = middle + 1
      else: #搜尋的值小於中間項，向左邊移動
         high = middle - 1
   return None

store = [152, 54, 49, 118, 141, 74, 175, 69, 155, 130]
number = random.choice(store)
length = len(store) - 1
newData = sorted(store)
print(newData)
print('Index:', searchInterpolation(newData, number, 0, length))
