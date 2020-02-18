#建立二維List - 以生成式配合range()函式
one, two, three = 11, 21, 31
number = [[one for one in range(one, 15)],
   [two for two in range(two, 25) ],
   [three for three in range(three, 35) ]]
#依據輸出每列的元素
print(number[0])
print(number[1])
print(number[2])
