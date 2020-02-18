#實作環狀佇列
class circularQueue:
   def __init__(self, maxSize):
      '''以List物件實作一個大小固定的佇列'''
      self.data = [None] * maxSize
      self.count = 0 #儲存於佇列的元素個數
      self.front = 0 #取得佇列的第一個元素
      self.rear = maxSize - 1

   def __len__(self):
      """Return the number of elements in the queue."""
      return self.count

   def isEmpty(self):
      return self.count == 0

   def isFull(self):
      return self.count == len(self.data)

   def show(self):
      '''顯示front、rear的變化情況'''
      print(' Front:', self.front, end = ', ')
      print('Rear:', self.rear)

   def dequeue(self):
      '''刪除元素'''
      if self.isEmpty() == False:
         answer = self.data[self.front]
         self.data[self.front] = None
         self.front = (self.front + 1) % len(self.data)
         self.count -= 1
         self.show()
         return answer
      else:
         print('空白佇列無法刪除')

   def enqueue(self, item):
      '''佇列後端新增一個元素，需要取得rear的索引'''
      if self.isFull() != True:
         #計算rear的位置
         self.rear = (self.rear + 1) % len(self.data)
         self.data[self.rear] = item #將新元素指向下一個位置
         self.count += 1
         print('{:4}'.format(item), end = '')
         self.show()
      else:
         print('佇列已滿無法新增')

cque = circularQueue(6)
Ary1 = [45, 136, 18, 62]
print('新增元素：')
for item in Ary1:
   cque.enqueue(item)
cque.dequeue()
cque.dequeue()
cque.enqueue(57)
cque.enqueue(13)
cque.enqueue(85)
cque.enqueue(37)
cque.enqueue(41)

cque.dequeue()
cque.dequeue()
cque.dequeue()
cque.dequeue()
cque.dequeue()
cque.dequeue()
cque.dequeue() #顯示無法刪除訊息

cque.enqueue(72)
cque.enqueue(123)
cque.enqueue(61)
cque.enqueue(57)
cque.enqueue(13)
cque.enqueue(85)
cque.enqueue(57)
#cque.enqueue(13)
#cque.enqueue(85)
