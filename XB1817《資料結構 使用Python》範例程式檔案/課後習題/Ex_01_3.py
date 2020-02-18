#實作3
class Student:
   def __init__(self, name):
      self.name = name

   def cost(self, course):
      if course <= 10:
         course *= 835
      elif course <= 12:
         course *= 750
      else:
         course *= 518
      return course

tom = Student('Tom')
print('學分費：', format(tom.cost(15), ','))
