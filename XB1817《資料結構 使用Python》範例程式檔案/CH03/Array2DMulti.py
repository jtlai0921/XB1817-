#兩個矩陣相乘
aryA = [[1, 2], [3, 4], [5, 6]] 
aryB = [[7, 9, 11], [8, 10, 12]]
#取得兩個矩陣的長度
X = len(aryA); Y = len(aryB); Z = len(aryB[0])
aryC = [] #空的List，存放aryA * aryB相乘結果 
   
for one in range(X):   
   for two in range(Z):      
      total = 0
      for three in range(Y):
         #依序將指定兩列的項目相加                
         total += aryA[one][three] * aryB[three][two]
      #以append()方法把每列的欄項目填入
      aryC.append(total)

#讀取相加後aryC所存放的內容
for one in range(X):
   for two in range(Z):
      print('{:>4d}'.format(aryC[one*Z + two]), end = '|')
   print()



