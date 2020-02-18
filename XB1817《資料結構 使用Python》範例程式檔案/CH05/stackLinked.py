#定義節點類別
class Nodes:
   '''初始化時取得節點，指標指向None'''
   def __init__(self, item = None):
      self.item = item
      self.next = None

class Stack:
   def __init__(self):
      self.top = None #維護Linked List頭節點
      self.size = 0   #追踪堆疊的項目數(長度)


   def push(self, item):
      '''堆疊頂端新增資料'''
      node = Nodes(item)
      #有首節點就把指標指向它，若無則以新節點為首節點
      if self.top:
         node.next = self.top
         self.top = node
      else:
         self.top = node
      self.size += 1
      return item

   def pop(self):
      '''移除堆疊頂端元素-有的話就移除它並回傳，沒有就以None回傳'''
      if self.top:
         item = self.top.item
         self.size -= 1
         #將移除元素的下一個變成頂端元素
         if self.top.next:
            self.top = self.top.next
         else:
            self.top = None
         return item
      else:
         return None

   def peek(self):
      '''回傳頂端元素'''
      if self.top:
         return self.top.item
      else:
         return None

name = ['Tom', 'Eric', 'Vicky', 'Peter', 'Charles']
st = Stack()
for pern in name:
   print(st.push(pern), end = ' ')
print('\n', st.pop())
print(st.peek())
