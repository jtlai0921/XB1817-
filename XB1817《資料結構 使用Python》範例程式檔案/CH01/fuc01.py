#定義函式
def funcMax(n1, n2):
    if n1 > n2:
        result = n1
    else:
        result = n2
    return result

# 呼叫函式
num1, num2 = eval(input('輸入兩個數值：'))
print('較大值', funcMax(num1, num2))
