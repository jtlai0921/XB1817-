number = int(input('輸入一個數值->'))
print('10進位：', number)
print('型別：', type(number))

# 配合format函式去除前綴字元
print(' 2進位', bin(number), format(number, 'b'))
print(' 8進位', oct(number), format(number, '>8o'))
print('16進位', hex(number), format(number, '>8x'))



