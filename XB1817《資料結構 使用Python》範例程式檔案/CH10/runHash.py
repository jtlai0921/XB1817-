def runHash(Ary):
   '''以除法為雜湊函數'''
   prime = 11 #設定質數和儲存空間為11
   #建立空的List物件，長度為11
   data = [None for k in range(prime)]
   for item in Ary:
      h = item % prime #除法取得餘數
      data[h] = item   #依餘數為索引來儲存元素
   return data
num = [4, 13, 21, 33, 63]
print('雜湊表：', runHash(num))