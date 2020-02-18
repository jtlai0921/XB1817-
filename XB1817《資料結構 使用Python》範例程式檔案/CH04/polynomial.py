class Polynomial:
   lstA = [0]* 20       #存放第一個輸入的多項式和計算結果
   lstB = [0]* 20       #存放輸入的多項式
   result = [0] * 20    #结果

   def getItem(self, pr):
      num = input('請依序輸入多項式的係數和指數(指數須小於10)->').split()
      for item in range(int(len(num)/2)):
         pr[int(num[2 * item + 1])] = int(num[2 * item])
      self.output(pr)

   def add(self, n1, n2):  #加法
      number = [n1[k] + n2[k] for k in range(20)]
      return number

   def minus(self, n1, n2):  #減法
      number = [n1[i] - n2[i] for i in range(20)]
      return number

   def multi(self, n1, n2):
      self.result = [0] * 20
      #n2分別與n1[0]~n1[9]相乘
      for k in range(10):
         #讀取n2[j] * n1[k]
         for j in range(10):
            self.result[k + j] = int(
                  self.result[k + j]) + int(n1[k] * n2[j])
      return self.result

   def output(self, n1):#輸出多項式
      n2 = ''
      for k in range(20):
         if n1[k] > 0:
            n2 += '+' + str(n1[k]) + 'X^' + str(k)
         if n1[k]< 0:
            n2 += '-' + str(-n1[k]) + 'X^' + str(k)
      print(n2[1::])

   def evaluate(self):   #依輸人的運算符號呼叫相關做計算
      print ('多項式的計算：')
      self.getItem(self.lstA)
      while True:
         opr = input('輸入運算符號(按-1結束)')
         if opr == '-1':
            return 0
         else:
            self.lstB = [0] * 20
            self.getItem(self.lstB)
            self.lstA = {'+' : self.add(
                  self.lstA, self.lstB), '-' : self.minus(
                  self.lstA, self.lstB), '*' : self.multi(
                  self.lstA, self.lstB)}.get(opr)
            print ('結果：', end = '')
            self.output(self.lstA)

poly = Polynomial()
poly.evaluate()
