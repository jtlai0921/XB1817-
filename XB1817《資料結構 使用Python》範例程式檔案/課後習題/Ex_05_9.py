#第五章實作(二)-9, 冪次方 num ^ x
def power(x, num):
   if num == 0:
      return 1
   else:
      return x * power(x, num - 1)

print(power(5, 3))