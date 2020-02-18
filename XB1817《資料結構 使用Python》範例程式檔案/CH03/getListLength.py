import sys #滙入sys模組提供位元組大小
data = [] #空的List
for k in range(3): #range()需給予參數值才能測試
   length = len(data) 
   sizeAry = sys.getsizeof(data) #實際大小為位元組
   print('Length:{0:3d}, \
         Size in bytes:{1:4d}'.format(length, sizeAry))
   data.append(None)