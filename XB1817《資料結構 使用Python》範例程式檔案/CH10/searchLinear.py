def searchLinear(Ary, target):
   index = 0   #取得欲搜尋項目的位置
   found = False #找到了搜尋元素就變更旗標
   #逐一比較，index < len(Ary)表示未找到
   while index < len(Ary) and not found:
      #找到Key回傳True，未找到就依據索引繼續往下找
      if Ary[index] == target:
         found = True
      else:
         index += 1
   return found
number = [117, 325, 54, 19, 63, 749, 41, 213]
print(searchLinear(number, 885))