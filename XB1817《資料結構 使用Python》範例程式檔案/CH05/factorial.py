def factorial(n):
   print('階乘函式 fact(n) 已經呼叫 {} 階乘'.format(n))
   if n == 1:
      return 1   #基醒情況，終止遞廻
   else:   #如果階乘是2(含)以上，呼叫自己的函式
      result = n * factorial(n-1)
      print('{:<2}階乘呼叫前一次的結果{:2} *'.format(n, n), end = '')
      print(' factorial({})'.format(n-1))
      return result

print('階乘計算結果：',factorial(5))
