#第二章，習題2
def student(name, *score, course = 5):
   # *運算子收集引數位置的參數，也就是5科分數
   print(name, end = ', ')
   total = sum(score) #直接呼叫sum()函式計算總分
   avg = total/course
   if avg >= 60:
      print('總分：{:4d}，平均：{:.3f}'.format(total, avg))
   else:
      print('平均未達60, 平均:{:.3f}'.format(avg))

#呼叫函式，將名稱和5科成績儲存於Tuple物件中
st1 = student('王小明', 78, 65, 91, 81, 43)
st2 = student('林一風', 61, 52, 45, 71, 43)
st32 = student('陳大雄', 91, 82, 53, 65, 43)