import random

class Node:
   def __init__(self, value):
      self.value = value
      self.next = next

class LinkedList:
   def __init__(self):
      self.head = None
      
   def addTail(self, value):
      '''加到最後節點'''
      if not self.head:
         self.head = Node(value)
         self.head.next = self.head
      else:
         newNode = Node(value)
         current = self.head
         #移動目前節點的指標
         while current.next != self.head:
            current = current.next
         #1.將目前節點的指標指向新節點
         current.next = newNode
         #2.將新節點的指標指向頭節點
         newNode.next = self.head

   def addHead(self, value):
      '''加到頭節點之前'''
      newNode = Node(value) #取得新節點的值
      current = self.head
      #新節點的鏈結指向原串列首節點
      newNode.next = self.head
      #判斷道節點是否存在
      if not self.head:
         newNode.next = newNode
      else:
         #移動目前節點的指標
         while current.next != self.head:
            current = current.next
         current.next = newNode
      self.head = newNode #新節點變成首節點

   def remove(self, key):
      '''刪除節點，以key傳遞'''
      #情形一：若首節點的值等於key，則刪除對象為首節點
      if self.head.value == key:
         current = self.head
         #移動指標
         while current.next != self.head:
            current = current.next
         #將目前節點的指標指向首節點的下一個節點
         current.next = self.head.next
         #首節點變更為下一個節點
         self.head = self.head.next
      else:
         #情形二：首節點以外的節點要被刪除
         current = self.head
         prev = None
         #移動指標找到刪除的節點
         while current.next != self.head:
            prev = current
            current = current.next
            if current.value == key:
               #前一個節點的指標指向目前節點的下一個節點
               prev.next = current.next
               current = current.next

   def josephus(self, step):
      '''依據間隔值step來移除節點'''
      current = self.head
      print('移除節點：', end = '')
      #確認鏈結串列要有節點
      while len(self) > 1:
         count = 1
         #移動指標走訪節點
         while count != step:
            current = current.next
            count += 1
         print('{:3}'.format(current.value), end = ' ')
         self.delItem(current) #step相同者被移除
         current = current.next

   def delItem(self, node):
      '''從指定節點開始刪除'''
      #情形一：從首節點開始移除
      if self.head == node:
         current = self.head
         #移動指標
         while current.next != self.head:
            current = current.next
         #將目前節點的指標指向首節點的下一個節點
         current.next = self.head.next
         #首節點變更為下一個節點
         self.head = self.head.next
      else:
         #情形二：首節點以外的節點要被移除
         current = self.head
         prev = None
         #移動指標找到刪除的節點
         while current.next != self.head:
            prev = current
            current = current.next
            if current == node:
               #前一個節點的指標指向目前節點的下一個節點
               prev.next = current.next
               current = current.next

   def __len__(self):
      current = self.head
      count = 0
      while current:
         count += 1
         current = current.next
         if current == self.head:
            break
      return count

   def splitItem(self):
      size = len(self)
      if size == 0:
         return None
      elif size == 1:
         return self.head
      mid = size // 2
      count = 0
      prev = None
      current = self.head
      while current and count < mid:
         count += 1
         prev = current
         current = current.next
      prev.next = self.head
      twoPart = LinkedList()
      while current.next != self.head:
         twoPart.addTail(current.value)
         current = current.next
      twoPart.addTail(current.value)
      self.show()
      print('\n')
      twoPart.show()

   def show(self):
      current = self.head
      print('\n環狀鏈結串列：')
      while current:
         print('{:3}'.format(current.value), end = '')
         current = current.next
         if current == self.head:
            break
      print()

circular = LinkedList()
for item in range(10, 20):
   random.seed()
   #產生10個1~100之間的亂數
   item = random.randint(1, 100) 
   circular.addTail(item)
circular.show()

circular.josephus(3)
circular.show()

#circular.splitItem()
#circular.show()