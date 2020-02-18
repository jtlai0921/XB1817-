#第10章-循序搜尋-實作題(一)
def smallValue(Ary):
   length = len(Ary)
   smallest = Ary[0] #先指定第一個項目為最小值
   #從第2個項目開始比對
   for item in range(1, length):
      if Ary[item] < smallest:
         smallest = Ary[item]
   return smallest

number = [79, 91, 86, 76, 97, 17, 57, 87, 56, 66, 4, 24]
print('最小值', smallValue(number))