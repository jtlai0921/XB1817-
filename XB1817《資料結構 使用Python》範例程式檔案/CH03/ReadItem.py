number = 25, 372, 65, 277, 541
for item in number:
   #指定欄寬為4，向左對齊
   print(format(item,'<4'), end = '')
print()
print('number 65的索引：', number.index(65))
