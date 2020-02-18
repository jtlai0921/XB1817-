total = 0 #儲存累加結果
for item in range(3, 21, 3):
   if item == 9:
      continue #中斷此次廻圈
   else:
      total += item
      print('計數器 = {0:2d}, 總和 = {1:2d}'.format(
         item, total))
else:
   print('for廻圈執行完畢')
