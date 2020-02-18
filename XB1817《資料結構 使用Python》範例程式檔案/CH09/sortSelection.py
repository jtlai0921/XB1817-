#選擇排序法 - 由小而大排序
def sortSelection(data, lg):
   #函式enumerate()取得陣列的索引
   for k, item in enumerate(data):
      #利用函式min()取得最小值
      minimum = min(range(k, lg), key = data.__getitem__)
      data[k], data[minimum] = data[minimum], item
      print(data) #觀看排序變化
   return data

def sortSelection2(data, lg):   #遞減排序
   #函式enumerate()取得陣列的索引
   for k, item in enumerate(data):
      #利用函式min()取得最小值
      maximum = max(range(k, lg), key = data.__getitem__)
      data[k], data[maximum] = data[maximum], item
      print(data) #觀看排序變化
   return data

number = [45, 21, 10, 18, 65, 33]
long = len(number)#取得陣列長度
print('未排序', number)
print('選擇排序', sortSelection2(number, long))