aryA = [[11, 12, 13, 14], [22, 24, 26, 28], [33, 36, 39, 41]]
lenC = len(aryA[0]) #取得二維陣列每欄長度

#讀取原來陣列
print('讀取原來陣列')
for row in aryA:
   for column in row:
      print('{0:>4d}'.format(column), end = '|')
   print()

#以List生成式將列、欄轉換-外部生成式依據矩陣列的長度讀取
trans = [ [row[column] for row in aryA]
          for column in range(lenC)]

print('列、欄轉換後陣列')
for row in trans:
   for column in row:
      print('{:>4d}'.format(column), end = '')
   print()
      
#zip()函式做列、欄轉換
aryB = (list(zip(*aryA)))
print('zip()函式-列、欄轉換後陣列')
for row in aryB:
   for column in row:
      print('{:>4d}'.format(column), end ='')
   print()
