def student(name, *score, course = 5):
   print(name, end = ', ')
   total = sum(score)
   avg = total/course
   if avg >= 60:
      print('總分：{:4d}，平均：{:.3f}'.format(total, avg))
   else:
      print('平均未達60, 平均:{:.3f}'.format(avg))

st1 = student('王小明', 78, 65, 91, 81, 43)
st2 = student('林一風', 61, 52, 45, 71, 43)
st32 = student('陳大雄', 91, 82, 53, 65, 43)