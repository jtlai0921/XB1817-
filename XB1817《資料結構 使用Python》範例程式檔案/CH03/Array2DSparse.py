#3-tuple處理稀疏矩陣

aryA = [[0, 0, 0, 27, 0], [0, 0, 13, 0, 0],
        [0, 41, 0, 0, 36], [52, 0, 9, 0, 0], [0, 0, 0, 18, 0]]

#取得矩陣列數、欄數
aryARow = len(aryA)
aryAColumn = len(aryA[0])
number = 0 #統計非零項目

print('讀取稀疏陣列')
for row in aryA:
   for column in row:      
      print('{0:>3d}'.format(column), end = '|')      
      if column != 0:
         number += 1
   print()

#處理稀疏矩陣
idx = 1 
aryB = [[None]*3 for item in range(number + 1)]
aryB[0][0] = aryARow
aryB[0][1] = aryAColumn
aryB[0][2] = number

#依據稀疏矩陣來取得非零元素的列、欄索引和值
for row in range(aryARow):
   for column in range(aryAColumn):
      if aryA[row][column] != 0:
         aryB[idx][0] = row+1
         aryB[idx][1] = column+1
         aryB[idx][2] = aryA[row][column]
         idx += 1

print('讀取壓縮後的稀疏陣列')
for row in range(number + 1):
   for column in range(3):      
      print(format(aryB[row][column], '>3d'), end = '|')      
   print()

