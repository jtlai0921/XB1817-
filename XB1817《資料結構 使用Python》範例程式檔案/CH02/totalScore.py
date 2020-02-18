#以陣列結構儲存分數，以while廻圈讀取List的元素
st1 = [98, 72, 65, 82]
item = 0
print('分數->', end = '')

#len()函式取得st1的長度，sum()將st1的元素加總
'''
while item < len(st1):
   print(format(st1[item], '<3d'), end = '')
   item += 1
else:
   print('\n總分', sum(st1))
'''
for item in st1:
    print(format(item, '<3d'), end = '')
else:
   print('\n總分', sum(st1))