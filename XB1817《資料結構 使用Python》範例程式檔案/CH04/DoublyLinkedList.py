#定義節點
class Score :
   def __init__(self, value):
      '''初始化Worker類別'''
      self.value = value
      self.Rnext = None #指向前一個節點
      self.Lnext = None #指向下一個節點

#定義雙向鏈結串列
class Student:

   def __init__(self):
      '''設屬性頭節點head和尾節點tail為None, count統計節點數'''
      self.head = None
      self.tail = None
      self.count = 0

   def precede(self, value):
      '''從頭節點插入資料'''
      grade = Score(value) #取得節點物件

      #如果頭節點為None表示它是一個空串列，設節點的頭、尾節點
      if self.head is None:
         self.head = grade
         self.tail = grade

      else: #若有頭節點

         # 1.把新節點的右鏈結指向串列的頭節點
         grade.Rnext = self.head

         # 2.將串列頭節點的左鏈結指向新節點
         self.head.Lnext = grade
         
         # 3.串列的頭節點指向新節點
         self.head = grade
      self.count += 1
   
   def append(self, value):
      '''從尾節點加入資料'''
      grade = Score(value) #取得新節點物件
      # 如果是空串列，就以新節點來產生
      if self.tail is None:
         self.head = grade
         self.tail = grade

      else:
         # 1.將串列尾節點的右鏈結指向新節點
         self.tail.Rnext = grade
         # 2.把新節點的左鏈結指向原串列的的尾節點
         grade.Lnext = self.tail
         # 3.原串列的尾節點變更為新節點
         self.tail = grade
      self.count += 1

   #依據指定位置之前插入新節點
   def insertAt(self, pos, value):
      
      #情形一：位置大於或等於零，呼叫precede()方法
      if pos <= 0:
         self.precede(value)
         return
      #情形二：位置大於節點數，呼叫append()方法
      elif pos > self.count:
         self.append(value)
         return

      current = self.head
      #依據傳入的位置參數讀取節點
      for courrent in range(pos):
         current = current.Rnext

      grade = Score(value)
      # 1.將新節點的右鏈結指向目前節點
      grade.Rnext = current
      # 2.將新節點的左鏈結指向目前節點的前一個節點
      grade.Lnext = current.Lnext
      # 3.將目前節點的左鏈結指向新節點
      current.Lnext = grade
      # 4.將目前節點的前一個節點的右鏈結指向新節點
      grade.Lnext.Rnext = grade
      self.count += 1
      del current #刪除目前的節點

   #從頭節點刪除
   def remove(self):
      #先判斷頭節點是否存在，若無表示它是空串列
      if self.head is None:
         print('無法移除節點')
      #若不是空串列，刪除後減少節點
      elif self.count == 1:
         self.head = None
         self.tail = None
         self.count -= 1
         return
      #目前指標指向頭節點的右鏈結-下一個節點
      current = self.head.Rnext
      #頭節點的右鏈結設為None
      self.head.Rnext = None
      #目前頭節點的左鏈結設為None
      self.head.Lnext = None
      #變更頭節點
      self.head = current
      self.count -= 1
      del current

   #從尾節點刪除
   def delete(self):
      if self.tail is None:
         print('無法移除節點')
      elif self.count == 1:
         self.head = None
         self.tail = None
         self.count -= 1
         return
      #取得尾節點的前一個節點
      current = self.tail.Lnext
      #設尾節點的左鏈結為None
      self.tail.Lnext = None
      #指標指向尾節點的前一個節點
      self.tail = current
      #設新的尾節點其右鏈結為None
      self.tail.Rnext = None
      self.count -= 1
      del current

   #輸出節點的資料
   def show(self):
      current = self.head
      while True:
         if current is None:
            break
         print('[', current.value,']-> ', end = ' ')
         current = current.Rnext
      print()

course = Student()
#新增於尾節點之後
course.append(78)
course.append(95)
course.append(84)
course.precede(67)
course.show()

#刪除節點
course.delete()
course.show()