#第四章 實作5

class Node :
   '''初始化Worker類別，屬性next鏈結下一個節點'''
   def __init__(self, value, next) :
      self.value = value
      self.next = next
   
      
#定義單向鏈結串列
class SLinkedList:
   def __init__(self):
      self.head = None
   
   def prepend(self, value):
      self.head = Node(value, self.head)

   def Output(self):
      count = 0
      cur = self.head
      while cur is not None:
         print(cur.value, end = ' ')
         cur = cur.next
         count += 1
      print('\n鏈結串列大小：', count)

single = SLinkedList()
single.prepend('Yellow')
single.prepend('Green')
single.prepend('Orange')
single.prepend('Red')
single.Output()