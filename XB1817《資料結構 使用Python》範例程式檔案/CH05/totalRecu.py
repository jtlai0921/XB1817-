#使用遞廻-計算連績數值的加總
def total_for_num(n):
   if n == 1:
      total = 1   #終止遞廻
   else:
      total = total_for_num(n - 1) + n   #遞廻關係式
   return total

print(total_for_num(10))