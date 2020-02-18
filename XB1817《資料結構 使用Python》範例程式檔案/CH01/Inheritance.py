# 參考範例《Inheritance.py》
class Father: #基礎類別
   def walking(self):
      print('多走路有益健康!')

class Son(Father): #衍生類別
   pass

Joe = Son()    #子類別實體(即物件)
Joe.walking()#
