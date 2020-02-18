from time import time

def appendTime(n):
   data = []
   start = time() #呼叫time()方法計算開始時間
   for k in range(n):
      data.append(None)
   end = time() #停止時間，以秒數計算
   result = end - start
   return result
def insertTime(n):
   data = []
   start = time() #呼叫time()方法計算開始時間
   for k in range(n):
      data.insert(k, None)
   end = time() #停止時間，以秒數計算
   result = end - start
   return result
print(appendTime(1000000))
print(insertTime(1000000))