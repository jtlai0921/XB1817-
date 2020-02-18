#自訂函式 -- 定義加總數字
'''
   使用range()函式
'''
def total(num1, num2, num3):
    result = 0 #儲存運算結果
    for item in range(num1, num2+1, num3):
        result += item #數值相加
    return result #回傳運算結果

print('計算數值總和：')
key = input('按y開始，按n停止-->')

while key == 'y':
    start = int(input('輸入起始值:'))
    finish = int(input('輸入終止值:'))
    step = int(input('輸入間距值:'))
    
    #呼叫自訂函式
    print('數值總和:{:,}'.format(
      total(start, finish, step)))

    key = input('按y開始，按n停止->')
