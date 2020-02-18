#實作單向鏈結串列，定義一個分數類別
class Score :
   #初始化Score類別
   def __init__(self, value, subject) :
      self.value = value      
      self.subject = subject

def TraversingNodes():
      global headNode
      ptrNode = headNode7
      if(ptrNode != None):
         while(ptrNode.subject != None):
            print(ptrNode.value)
            ptrNode = ptrNode.subject
         print(ptrNode.value)
      else:
         print('空白的節點')

#產生Score物件 chin, eng, math
s1, s2, s3 = eval(input('請輸入國文、英文、數學分數，並以逗點分隔：\n'))
math = Score(s3, None)
eng = Score(s2, math)
chin = Score(s1, eng)
headNode = chin

print('[', chin.value, ']-> [', eng.value,
      ']-> [', math.value, ']-> None')  

