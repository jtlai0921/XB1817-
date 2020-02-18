class Queue: #以List 實做Queue
   def __init__(self):
      self.items = []

   def dequeue(self): #佇列前端刪除項目
      if len(self.items) == 0:
         raise ValueError('佇列是空的')
      else:
         value = self.items.pop(0)
         print('\n刪除佇列項目', value)

   def enqueue(self, data): #佇列後端加入項目
      self.items.append(data)

   def front(self): #查看佇列前端
      print('前端', self.items[0])

   def rear(self): #查看佇列後端
      print('後端', self.items[-1])

   def show(self): #輸出佇列項目
      print('佇列', self.items, end = '')

que = Queue()
data = ['Tom', 'Judy', 'Bob', 'Peter']
for item in data:
   que.enqueue(item)
print()
que.show()
que.dequeue()
que.show()
