#第九章 實作第三題選擇排序法-遞減
def SelectionSort(Ary):
   for k in range(0, len(Ary) - 1):
      index = k #儲存最大數字的索引
      for j in range(k + 1, len(Ary)):
         if Ary[j] > Ary[index]:
            index = j
      if index != k:
         Ary[k], Ary[index] = Ary[index], Ary[k]
   return Ary

source = [185, 625, 134, 47, 731, 125, 42, 416]
print('選擇排序法-遞減', SelectionSort(source))
