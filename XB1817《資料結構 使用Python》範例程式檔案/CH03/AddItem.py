ambit = 5 # 設定range()函式範圍
score = [] #建立空的串列
# 以for廻圈讀取資料
print('請輸入5個數值：')
for item in range(ambit):
   line = input() #取得輸入數值
   if line:
       data = int(line) #int()函式轉為數值
   score.append(data) #將輸入數值新增到score
else:
   print('已輸入完畢')

#輸出資料
item = 0
print('輸入資料有', end = '-->')
while item < len(score):   
   print('{:4d}'.format(score[item]), end = '')
   item += 1
