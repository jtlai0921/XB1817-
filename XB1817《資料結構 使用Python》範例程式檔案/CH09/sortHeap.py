def sortHeap(Ary):
   '''轉陣列轉為堆積的方法就是從最後一個有兒子的父節點leastParent開始'''
   length = len(Ary) - 1 #length = 8-1 = 7
   leastParent = length // 2 #取得位置為索引3

   #將目前待排序數列築成一個最大堆積
   for k in range (leastParent, -1, -1):
      #由range(3, -1, -1)得索引k = 3, 2, 1, 0，表示它們皆有兒子
      heapDown(Ary, k, length)

  # 走訪整個陣列依，逐步把每個最大值根節點與最後一個項目交換，並調整成最大堆積
   for k in range (length, 0, -1):   #依索引7, 6, 5, 4, 3, 2, 1
      if Ary[0] < Ary[k]: 
         #將根節點與與未排序數列中最後一個節點做對調
         swap(Ary, 0, k)
         heapDown(Ary, 0, k - 1)

#往下做調整，已排序過的元素會被忽略-first(left), last(right)
def heapDown(Ary, first, last):
   '''找出大兒子-依傳入的索引與其他子節點的大兒子做比較'''
   largest = 2 * first + 1  #設左子節點為最大兒子
   '''依據二元樹的編號，根節點為first，則左子樹是2*first，右子樹就是2*first+1
   由於索引是從零開始，所以左子樹的編號是1而非2'''

   #想法子找出大兒子，包括含有左、右兒子的父節點，找到了大兒子讓它能上移一層
   while largest <= last:
      '''largest < last, 表明並沒有到最後一個節點
         Ary[largest], Ary[largest + 1]表示左兒子<右兒子
      '''
      if (largest < last) and \
            (Ary[largest] < Ary[largest + 1]):
         #停留在Ary[largest]=95, Ary[last]=23
         largest += 1   #找出大兒子，指向右兒子的編號也包含

      # 大兒子比父節點大，就視它為大兒子，兩者對調
      if Ary[largest] > Ary[first]:
         swap(Ary, largest, first)
         first = largest; #將大兒子上移一層
         largest = 2 * first + 1
      else:
         break

# 將傳入的陣列元素做交換
def swap(Ary, x, y):
   Ary[x], Ary[y] = Ary[y], Ary[x]
   #print('Swap', Ary)


source = [58, 46, 72, 23, 130, 35, 12, 95]
sortHeap(source)
print('堆積排序法', source)
