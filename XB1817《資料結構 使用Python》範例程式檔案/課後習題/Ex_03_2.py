#第三章 實作2

number = [] #空的List物件
number = [item for item in range(1, 100)
   if item % 5 == 0]
print(number)