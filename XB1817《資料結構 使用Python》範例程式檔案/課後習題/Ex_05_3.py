#第五章, 實作第一題-將字串反轉

class Stack: #以List 實做Stack
   def __init__(self):
      self.items = []

   #判斷堆疊是否為空白
   def isEmpty(self):
      if len(self.items) == 0:
         return True
      else:
         return False

   #呼叫BIF len()函式來取得堆疊長度
   def size(self):
      return len(self.items)

   #查看堆疊頂端項目並回傳其值
   def peek(self):
      assert not self.isEmpty(),\
         '無法以peek()方法查看空白堆疊'
      #指定List物件的最後一個元素為堆疊頂端的項目
      return self.items[-1]

   #彈出堆疊頂端的項目-呼叫List物件的pop()方法移除最後一個元素
   def pop(self):
      assert not self.isEmpty(),\
         '無法以pop()方法查看空白堆疊'
      return self.items.pop()

   #將項目推入堆疊頂端-呼叫List的append()方法加到末端
   def push(self, data):
      self.items.append(data)
      return data

#定義反轉字串函式-使用堆疊
def strReverse(stack, word):
   for ch in range(len(word)):
      stack.push(word[ch])
   rev_word = ''
   while not stack.isEmpty():
      rev_word += stack.pop()
   return rev_word

#產生Stack物件
myStack = Stack() #產生Stack物件
msg = 'Python'
print(strReverse(myStack, msg))

