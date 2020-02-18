#定義節點
class Score :
   '''初始化Worker類別，屬性next鏈結下一個節點'''
   def __init__(self, value) :
      self.value = value
      self.next = None
   
      
#定義單向鏈結串列
class Student:
   def __init__(self):
      self.head = None   #設頭節點head為None
   
   #取得長度
   def getLength(self):
      curNode = self.head #頭節點設為目前節點
      length = 0
      #讀取節點計算長度
      while curNode is not None:
         length += 1
         curNode = curNode.next
      return length
   
   #是不是有節點
   def isEmpty(self):
      if self.head is None:
         return True
      else:
         return False
   
   #從頭節點插入資料-value=>67, next=>None
   def addHead(self, grade):
      tmp = self.head #頭節點先以tmp暫存
      self.head = grade #頭節點指標指向新節點
      self.head.next = tmp #新節點指向下一個節點
      del tmp #刪除暫存指標
   
   #在兩個節點之間插入新項目
   def insertPos(self, grade, location):
      
      prior = None #前一個節點
      
      #判斷插入的位置是否為合宜位置， 若為零就變更為頭節點
      if location < 0 or location > self.getLength():
         raise IndexError('插入的位置不對')
      elif location is 0:
         self.addHead(grade)
      curNode = self.head
      curPos = 0 #取得目前節點的位置
      
      while True:
         #指定位置和目前節點符合就插入節點
         if curPos == location:
            #將grade加到指定節點(84)的前一個節點(95)位置
            prior.next = grade
            #將新節點的指標指向目前節點(84)
            grade.next = curNode
            break
         prior = curNode
         curNode = curNode.next
         curPos += 1
         
   #從尾節點加入資料
   def addEnd(self, grade):
      '''判斷頭節點是否為None，若是的話將第一個節點設為頭節點
         head=>78=>Noe
      '''
      if self.head is None:
         self.head = grade
      else:
         tail = self.head
         #讀取資料若下一個節點為None就是尾節點
         while True:
            if tail.next is None:
               break
            tail = tail.next
         tail.next = grade
   
   #刪除頭節點
   def removeHead(self):
      if self.isEmpty() is False:
         #刪除頭節點前先變更指標，將它指向下一個節點，然後本身指標變成None
         priorHead = self.head
         self.head = self.head.next
         priorHead.next = None
      else:
         print('無法刪除節點')
   
   #刪除某一個指定節點
   def removeAt(self, location):
      #判斷插入的位置是否為合宜位置， 若為零就變更為頭節點
      if location < 0 or location >= self.getLength():
         raise IndexError('指定的位置不對')
      elif self.isEmpty() is False:
         #指定的位置為零，呼叫removeHead()方法刪除頭節點
         if location is 0:
            self.removeHead()
         curNode = self.head
         curPos = 0

         while True:
            if curPos == location:
               #將前一個節點的指標指向目前(欲刪除)節點
               prior.next = curNode.next
               #將欲刪除節點指標設為None
               curNode.next = None
               break
            #刪除節點後，將前一個節點的指標指向目前節點
            prior = curNode
            curNode = curNode.next
            curPos += 1
            
   #刪除尾節點
   def removeEnd(self):
      tail = self.head
      while tail.next is not None:
         prior = tail
         tail = tail.next
      prior.next = None
      
   #輸出節點的內容
   def show(self):
      current = stu.head
      while True:
         if current is None:
            break
         print('[', current.value,']-> ', end = ' ')
         current = current.next      
      print()

#產生鏈結串列物件，呼叫append()方法新增節點
one = Score(78)
stu = Student()
stu.addHead(one)

two = Score(95)
stu.addEnd(two)

three = Score(84)
stu.addEnd(three)

four = Score(67)
stu.addEnd(four)
stu.show()

#stu.removeEnd()#刪除尾節點
stu.removeAt(1)

stu.show()
