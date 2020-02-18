import ctypes

AryType = ctypes.py_object * 5
data = AryType()

#1.給予陣列None來完成初始化
for item in range(5) :
   data[item] = None

#2.給予陣列的元素
data[1], data[2], data[4] = 27, 652, 317

for item in data :
   print(item, end = ', ')