#改善循序搜尋：1.將資料排序；2.大於Key就不再往下查找
import random

def searchLinear_sorted(Ary, target):
   index = 0   #取得欲搜尋項目的位置
   #逐一比較，index < len(Ary)表示未找到
   for index in range(len(Ary)):
      #找到Key回傳True，未找到就依據索引繼續往下找
      if Ary[index] == target:
         return True
      #比對值大於key就不再往下查找
      elif Ary[index] > target:
         return False
   return False

number = random.sample(list(range(1, 100)), 12)
#number = [15, 39, 25, 63, 54, 34, 16, 70, 71, 77, 91, 81]
newItem = sorted(number)
print(newItem)
print(searchLinear_sorted(newItem, 25))
