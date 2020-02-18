#定義謝耳排序
def sortShell(ary):
   cleft = len(ary) // 2 #取間值隔整數
   #間隔值大於零的情形下
   while cleft > 0:
      #依間隔值來讀取陣列內容並呼叫插入排序法進行排序
      for start in range(cleft):
         sortInsertforGap(ary, start, cleft)

         print('間隔值 =', cleft,'\n陣列：', ary)
         cleft = cleft // 2 #調整為更小的間隔

#插入排序法
def sortInsertforGap(ary, start, gap):
    for k in range(start + gap, len(ary), gap):
        current = ary[k]
        pos = k #取得索引位置
        #依左大右小的規則，調整元素位置
        while pos >= gap and ary[pos - gap] > current:
            ary[pos] = ary[pos - gap]
            pos = pos - gap
        ary[pos] = current

source = [45, 26, 38, 92, 67, 13, 56, 71]
sortShell(source)
print('謝耳排序：', source)