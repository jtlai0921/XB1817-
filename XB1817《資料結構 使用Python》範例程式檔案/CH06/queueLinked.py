#以鏈結串列實作佇列
class Node: #鏈結串列的節點
   def __init__(self, item):
      self.item = item
      self.next = None

#建立Queue類別
class Queue:
   def __init__(self):
      '''設首、尾節點為None'''
      self.qhead = None 
      self.qtail = None

   def isEmpty(self): #是否為空佇列
      return self.qhead is None

   def enqueue(self, item):
      #不是空佇列才新增節點
      newNode = Node(item)
      if self.isEmpty():
         self.qhead = newNode
      else:
         #佇列尾端指標指向新節點
         self.qtail.next = newNode
      #從佇列後端新增節點
      self.qtail = newNode

   def dequeue(self):
      if self.qhead is not None:
         #目前指標指向首節點
         current = self.qhead
         #首節點指標指向下一個節點
         self.qhead = current.next
      print('刪除項目', current.item)

   def fornt(self): #取得佇列前端的項目
      if self.qhead is None:
         print('佇列是空的')
      else:
         print('前端', self.qhead.item)

   def rear(self): #取得佇列後端的項目
      current = self.qhead
      while current:
         if current.next is None:
            print('後端', current.item)
         current = current.next

   def show(self):
      current = self.qhead
      print('佇列：', end = '')
      while current:
         print(current.item, end = ' ')
         if current.next is None:
            break
         current = current.next
      print()

que = Queue()
number = ['one', 'two', 'three', 'four', 'five']
for k in number:
   que.enqueue(k)
que.show()
que.dequeue()
que.dequeue()
que.dequeue()
que.dequeue()
que.dequeue()
que.show()
que.fornt()
que.rear()
que.enqueue(256)
que.show()