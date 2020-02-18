#第六章 實作題二
class aryQueue: #以List 實做Queue
   def __init__(self):
      self.items = []

   def isEmpty(self):
      if self.items == []:
         print('Queue is Empty!!')

   def size(self):
      return len(self.items)

   def dequeue(self): #佇列前端刪除項目
      if len(self.items) == 0:
         raise ValueError('佇列是空的')
      else:
         value = self.items.pop()
         print('\n刪除佇列項目', value)

   def enqueue(self, data): #佇列後端加入項目
      self.items.insert(0, data)

   def show(self): #輸出佇列項目
      print('佇列', self.items, end = '')

nums = aryQueue()
data = ['one', 'two', 'three']
nums.isEmpty()
for k in data:
   nums.enqueue(k)
nums.show()
print()
print('佇列大小：', nums.size())