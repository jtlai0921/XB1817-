#二維陣列-以列為主

array2D = [[11, 12, 13, 14],
   [22, 24, 26, 28], [33, 35, 37, 39]]

#讀取以列為主的二維陣列
print('以列為主')
for idx, one in enumerate(array2D):
   print('第 {0} 列- '.format(idx), end = '')   
   for two in one:
      print(format(two, '<3'), end = '')
   print()
   
#讀取以欄為主的二維陣列
print('以欄為主')
print([[row[column] for row in array2D]
       for column in range(4)])
'''
print('\n'.join([''.join(['{0:<3}'.format(row[column])
      for row in array2D]) for column in range(4)]))'''
