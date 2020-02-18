#兩個矩陣相加
aryA = [[5, 3, 2], [11, 7, 13], [9, 13, 15]]
aryB = [[1, 6, 8], [4, 12, 16], [9, 18, 21]]
aryC = [] #空的List物件，存放兩個矩陣相加的結果

#append()方法將相加後的元素存放到aryC
for row in range(3):
   aryC.append([]) #產生空白的3列
   for column in range(3):
      #依序將指定兩列的項目相加
      element = aryA[row][column] + aryB[row][column]
      #以append()方法把每列的欄項目填入
      aryC[row].append(element)
      
#讀取相加後aryC所存放的內容   
for idx, one in enumerate(aryC):
   print('第', idx, '列', end = '|')
   for two in one:
      print(format(two, '>4d'), end = '|')
   print()
