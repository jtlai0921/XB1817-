#先以Python List實作堆疊
class Stack:
   def __init__(self):
      self.stackOpr = []
   
   def push(self, value): #
      self.stackOpr.append(value)
   
   def pop(self):
      if len(self.stackOpr) == 0:
         raise ValueError('堆疊是空的')
      else:
         k = self.stackOpr.pop()
      return (k)
   
   def peek(self):
      return (self.stackOpr[-1])
   
   def show(self):
      print('堆疊', self.stackOpr, end = ' ')

#繼承堆疊，將中序轉為後序
class InfixToPostfix(Stack):
   def __init__(self, express):
      Stack.__init__(self)
      self.result = []
      self.prece = {}
      #設定運算子的優先等級
      self.prece['*'] = 3
      self.prece['/'] = 3
      self.prece['+'] = 2
      self.prece['-'] = 2
      self.prece['('] = 1
      self.newExpress = express.split()

   def convert(self):
      #for廻圈讀取分割後的運算式
      for token in self.newExpress:
         #print(token, end = ' ')

         #情形一：字串的isalpha()方法判斷是否符合unicode所定義
         if token.isalpha():
            self.result.append(token)

         #情形二：遇到右括號先壓入堆疊中
         elif token == '(':
            self.push(token)
            
         #情形三：若是左括號以pop()方法彈出堆疊並放入List中
         elif token == ')':
            while not self.peek() == '(':
               k = self.pop()
               self.result.append(k)
            self.pop()

         else:
            #非上述情形就以while廻圈檢查堆疊頂端元素
            while len(self.stackOpr) > 0 \
                  and self.prece[self.peek()] \
                  >= self.prece[token]:
               other = self.pop()
               self.result.append[other]
            self.push(token)
            
      #print()

   def show(self):
      while not len(self.stackOpr) == 0:
         k = self.pop()
         self.result.append(k)
      print(' '.join(self.result))


#opr = InfixToPostfix('A - ( ( B * ( C + D ) ) / E )')
opr = InfixToPostfix('A - ((B * ( C + D )) / E')
opr.convert()
opr.show()

