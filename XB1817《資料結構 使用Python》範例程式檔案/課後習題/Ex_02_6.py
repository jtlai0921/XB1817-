#第二章，習題6
total = 1
number = int(input('輸入一個整數，計算階乘和->'))
for item in range(1, number+1):
   total *= item
   print(total)