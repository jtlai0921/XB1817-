#以遞廻求最大公倍數
def gcd(n1, n2):
   #如果n1<n2就置換
   if (n1 < n2):
      n1, n2 = n2, n1
   #如果n1除n2的餘數為0，n2就是最大公倍數
   if n1 % n2 == 0:
      return n2   #基本案例，終止遞廻
   else:
      return gcd(n2, n1%n2)   #遞廻關係式
print('GCD is',gcd(36, 42))
