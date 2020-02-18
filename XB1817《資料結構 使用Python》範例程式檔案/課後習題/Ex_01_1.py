# 實作1
def calcNum(num1, num2):
   r1 = num1 + num2
   r2 = num1 * num2
   r3 = num1 / num2
   r4 = num1 % num2
   return r1, r2, r3, r4

n1, n2 = eval(input('輸入兩個數值，以逗點隔開->'))
print('計算結果', calcNum(n1, n2))