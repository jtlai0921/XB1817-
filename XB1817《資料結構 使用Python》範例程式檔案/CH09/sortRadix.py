import math

def sortRadix(Ary, radix=10):
   #用digit位數可表示任意整數-取得最大整數
   digit = int(math.ceil(math.log(max(Ary)+1, radix)))
   #list生成式來存放
   bucket = [[] for item in range(radix)]
   for k in range(1, digit + 1): 
      for elem in Ary:
         #獲得從低到高的整數
         bucket[elem%(radix ** k) // \
            (radix **(k - 1))].append(elem)
      del Ary[:]
      for value in bucket:
         Ary.extend(value) # 桶合併
      bucket = [[] for item in range(radix)]

source = [59, 93, 17, 24, 70, 156, 185, 264, 566, 55, 86, 123]
sortRadix(source)
print(source)
