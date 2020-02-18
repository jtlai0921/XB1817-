from collections import deque   #匯入雙佇列模組

data = deque([97, 92, 63, 55, 124], 4)

print('雙佇列', data)
print('移除最右端', data.pop())
print('Index:', data.index(63))
data2 = deque(data, 6)
data2.append('One')
data2.append('Two')
data2.appendleft(27)
print('雙佇列', data2)

data2.rotate(1)
print('\n右旋轉：', data2)
data2.rotate(-2)
print('左旋轉：', data2)

data2.remove(92)
rd = reversed(data2)
for item in rd:
   print(item, end = ' ')
