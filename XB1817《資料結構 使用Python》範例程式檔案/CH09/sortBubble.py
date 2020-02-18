#氣泡排序法 - 遞增排序
#氣泡排序法
def sortButtle(data, long): #遞增
   #以移動指標方式來移動
   for k in range(long - 1, 0, -1):
      #讀取指標的項目並比較大小
      for item in range(k):
         if data[item] > data[item + 1]:
            #前一個項目比後一個項目大就彼此互換
            data[item], data[item + 1] = \
               data[item + 1], data[item]
            print(data)
   return data

def sortButtle2(data, long): #遞減
   #以移動指標方式來移動
   for k in range(long):
      #讀取指標的項目並比較大小
      for item in range(k):
         if data[item] < data[item + 1]:
            #前一個項目比後一個項目大就彼此互換
            data[item], data[item + 1] = \
               data[item + 1], data[item]
            print(data)
   return data

data = [25, 33, 11, 78, 65, 57]
long = len(data)
print('未排序', data)
print('氣泡排序', sortButtle(data, long))
