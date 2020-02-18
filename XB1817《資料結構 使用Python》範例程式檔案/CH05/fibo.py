def fibo(n):
   if n == 0:
      return 0   #基本案例，終止遞廻
   elif n == 1:
      return 1   #基本案例，終止遞廻
   else:
      return fibo(n - 1) + fibo(n - 2)   #遞廻關係式

num = 1
for k in range(12):
   print(fibo(num), end = ' ')
   num += 1