#第九章 實作第二題-插入排序法-遞減
def InsertionSort(Ary):
   length = 0
   for length in range(1, len(Ary)):
      item = Ary[length]
      idx = length
      while idx > 0 and item < Ary[idx - 1]:
         Ary[idx] = Ary[idx - 1]
         idx += -1
      Ary[idx] = item
   return Ary

source = [185, 625, 134, 47, 731, 125, 42, 416]
print('插入排序法-遞增', InsertionSort(source))
