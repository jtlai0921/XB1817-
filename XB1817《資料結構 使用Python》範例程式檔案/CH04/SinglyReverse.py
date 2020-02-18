import random

class Numbers:
   def __init__(self, item, next):
      self.item = item
      self.next = next

#定義單向鏈結串列
class SLinkedList:
   def __init__(self):
      self.head = None

   def isEmpty(self):
      return self.head is None

   def prepend(self, item):
      '''新節點加到第一個節點之前'''
      self.head = Numbers(item, self.head)

   def append(self, item):
      '''新節點加到末端'''
      if self.head is None:
         self.head = Numbers(item, None)
         return
      current = self.head
      while current.next is not None:
         current = current.next
      current.next = Numbers(item, None)

   def find(self, pred):
      current = self.head
      while current is not None:
         if pred(current.item):
             return current.item
         current = current.next
      return None

   def nodeSwap(self, N1, N2):
      if N1 == N2:
         raise ValueError('兩個節點相同')
      prev1 = prev2 = None
      current1 = self.head
      
      while current1 and current1.item != N1:
         prev1 = current1
         current1 = current1.next
      
      current2 = self.head
      
      while current2 and current2.item != N2:
         prev2 = current2
         current2 = current2.next
      if not current1 or not current2:
         return
      #情形一：要置換的兩個節點，其中一個是首節點
      if prev1:
         #將前一個節點的指標指向目前節點
         prev1.next = current2
      else:
         #N2變成首節點
         self.head = current2

      #情形二：要置換的兩個節點都不是首節點
      if prev2:
         #將前一個節點的指標指向目前節
         prev2.next = current1
      else:
         self.head = current1
      current1.next, current2.next = \
         current2.next, current1.next

   def regress(self):
      '''將鏈結串列的節點反轉'''
      prev = None
      #從首節點開始，移動指標走訪節點
      while self.head is not None:
         #從首邊點開始走訪
         current = self.head
         #將目前節點移向下一個節點
         self.head = current.next
         #目前節點的指標指向上一個節點
         current.next = prev
         #將前一個節點變更為目前節點
         prev = current
      #首節點移向前一個節點
      self.head = prev

   def show(self):
      '''輸出鏈結串列'''
      current = self.head
      while current is not None:
         print('%-9s' %current.item, end = '')
         if current.next is not None:
            print(end = '')
         current = current.next
      print()

if __name__ == '__main__':
   single = SLinkedList()
   print('鏈結串列：')
   name = ['Sandy', 'Judy', 'Charles', 'Peter', 'Evie']
   for item in name:
      single.append(item)
   single.show()

   single.nodeSwap('Charles', 'Evie')
   print('兩個節點交換')
   single.show()

   single.regress()
   print('反轉節點：')
   single.show()