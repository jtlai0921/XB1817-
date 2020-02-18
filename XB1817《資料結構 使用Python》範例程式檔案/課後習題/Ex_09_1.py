#第九章 實作第一題-氣泡排序法
def bubbleSort(Ary):
   swapped = True
   while swapped:
      swapped = False
      for item in range(1, len(Ary)):
         if Ary[item - 1] < Ary[item]:
            Ary[item], Ary[item - 1] = Ary[item - 1], Ary[item]
            swapped = True
      print(Ary, end = ' ')
      print()
   return Ary

source = [85, 34, 11, 73, 65, 42, 126]
print('氣泡排序法-遞增', bubbleSort(source))
