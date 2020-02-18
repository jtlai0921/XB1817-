# 第三章，實作3
ary2D = ['Tomas', [78, 96, 62], 
         'Eric', [88, 64, 63],
         'Sandy', [55, 92, 67]]

for first in ary2D:
   if isinstance(first, list):
      for second in first:
         print('{:3d}'.format(second), end = '')
      print()
   else:
      print('{:6}-'.format(first), end = '')
