#第四章 實作6 --定義雙向鏈結串列
class Student:

   class Name:
      def __init__(self, title):
         '''初始化Worker類別'''
         self.title = title
         self.Rnext = None 
         self.Lnext = None 
      
   def __init__(self):
      '''設屬性頭節點head和尾節點tail為None, count統計節點數'''
      self.head = None
      self.tail = None
      self.count = 0

   def append(self, title):
      name = self.Name(title) #取得新節點物件
      # 如果是空串列，就以新節點來產生
      if self.tail is None:
         self.head = name
         self.tail = name

      else:
         # 1.將串列尾節點的右鏈結指向新節點
         self.tail.Rnext = name
         # 2.把新節點的左鏈結指向原串列的的尾節點
         name.Lnext = self.tail
         # 3.原串列的尾節點變更為新節點
         self.tail = name
      self.count += 1

   def Output(self):
      current = self.head
      while True:
         if current is None:
            break
         print('[', current.title,']-> ', end = ' ')
         current = current.Rnext
      print()

stu = Student()
data = ['Tom', 'Adny', 'Vicky', 'Jan']
for item in data:
   stu.append(item)
stu.Output()
