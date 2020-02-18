#實作2
def score(n1, n2, n3):
   total = n1 + n2 + n3
   avg = total / 3
   if avg >= 60:
      print('總分：{}, 平均：{:.3f}, 過關'.format(
            total, avg))
   else:
      print('總分：{}, 平均：{:.3f}, 要加油'.format(
            total, avg))

s1, s2, s3 = eval(input('請輸入3科分數->'))
score(s1, s2, s3)
