#插入排序法 - 由小而大遞增排序
def sortInsert(data, lg):
   for k in range(1, lg):
      preid = k - 1 #取得欲比較的前(preid)、後項(k)索引
      key = data[k] #設當前的項目為鍵值
      # 當前一項的值 > 後一項的值時
      while data[preid] > key and preid >= 0:
         data[preid + 1] = data[preid] #移向前項索引之前
         preid -= 1
      data[preid + 1] = key #data[preid] < key，表示key值較大
      print(data)
   return data

number = [78, 56, 43, 12, 63, 23]
long = len(number)#取得陣列長度
print('未排序', number)
print('插入排序法', sortInsert(number, long))

