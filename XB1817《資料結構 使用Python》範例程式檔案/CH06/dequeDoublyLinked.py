#定義鏈結串列的節點
class DqNode:

   __slots__ = 'elem', 'Lnext', 'Rnext'

   def __init__(self, elem, Lnext, Rnext):
      '''初始化三個欄位'''
      self.elem = elem
      self.Lnext = Lnext   #指向前一個節點的指標
      self.Rnext = Rnext   #指向下一個節點的指標

class DoublyLinked:
   def __init__(self):
      '''建立空白的List物件'''
      self.front = DqNode(None, None, None)
      self.rear = DqNode(None, None, None)
      #self.front = DqNode(None)
      #self.rear = DqNode(None)
      #首節點的右指標指向後端
      self.front.Rnext = self.rear
      #尾節點左指標指向前端
      self.rear.Lnext = self.front  
      self.size = 0                # 計算項目的個數

   def __len__(self):
      return self.size

   def isEmpty(self):
      return self.size == 0

   def insertBetween(self, item, precede, follow):
      '''找到鏈結串列左(precede)、右(follow)兩個鄰居，加入元素並存入新節點'''
      newest = DqNode(item, precede, follow)
      #前一個節點的右指標指向新節點
      precede.Rnext = newest
      #下一個節點的左指標指向新節點
      follow.Lnext = newest
      self.size += 1
      print(newest.elem, end = ' ')
      return newest

   def remove(self, node):
      '''刪除無標記的節點並回傳其值'''
      precede = node.Lnext
      follow = node.Rnext
      #前一個節點的右指標指向欲刪節點的下一個節點
      precede.Rnext = follow
      #下一個節點的左指標指向欲刪節點的前一個節點
      follow.Lnext = precede
      self.size -= 1
      elem = node.elem   # 取得刪除的元素
      #欲刪除節點的左、右指標和值都歸成None
      node.Lnext = node.Rnext = node.elem = None 
      return elem

class dequeDLinked(DoublyLinked):
   def getfirst(self):
      print('First:', self.front.Rnext.elem, end = '')

   def getlast(self):
      print(', Last:', self.rear.Lnext.elem)

   def appendFirst(self, item):
      '''新增項目會加到首節點之後'''
      self.insertBetween(item, self.front, self.front.Rnext)
      return item

   def appendLast(self, item):
      '''新增項目會加到尾節點之前'''
      self.insertBetween(item, self.rear.Lnext, self.rear)
      return item

   def deleteFirst(self): #刪除第一個節點
      return self.remove(self.front.Rnext)

   def deleteLast(self):  #刪除最後一個節點
      return self.remove(self.rear.Lnext)

   def show(self):
      current = self.front
      print('佇列：', end = '')
      while current:
         print(current.elem, end = ' ')
         if current.Rnext is None :
            break
         current = current.Rnext
      print('\n佇列大小：', self.size)

pern = dequeDLinked()
score = [78, 95, 86, 69]
name = ['Mary', 'John', 'Peter', 'Sandy']

for k in score:
   pern.appendFirst(k)

for j in name:
   pern.appendLast(j)

pern.deleteFirst()
pern.deleteLast()

pern.show()
pern.getfirst()
pern.getlast()
