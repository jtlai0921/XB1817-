from decimal import Decimal    #滙入模組的方法
num1 = Decimal('0.5534')
num2 = Decimal('0.427')
num3 = Decimal('0.37')
print('相加', num1 + num2 + num3)    # 1.3504
print('相減', num1 - num2 - num3)    # -0.2436
print('相乘', num1 * num2 * num3)    # 0.087431666
print('相除', num1 / num2)
