#第二章，習題5
total = 0
for item in range(101, 200, 2):
   if item % 2 == 1:
      total += item
else:
   print('101~200奇數和', total)
