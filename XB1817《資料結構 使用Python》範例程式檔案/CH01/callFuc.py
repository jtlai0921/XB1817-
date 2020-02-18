'''
   Python傳遞引數依物件的可變和不可變做傳遞
   可變物件
'''
def passFun(name, score):
    
    #只有內部的名字被改變
    name = 'Tomas'
    print(name, end = ', ')
    #新增一個分數，也影響函式之外的串列
    score.append(47)
    print('分數', score)

#呼叫函式
title = 'Mary'
value = [75, 68]
passFun(title, value)
print(title, ', 分數', value)