#實作單向鏈結串列，定義一個分數類別
class Score :
   #初始化Score類別
   def __init__(self, value, subject) :
      self.value = value
      self.subject = subject
   
   #走訪節點並統計節點數
   def TraversingNodes(self):
      global headNode #全域變數
      curNode = headNode #將頭節點設為目前節點
      fields = 0 #統計走訪的節點
      #目前節點非None，再以while廻圈取得節點中儲存的資料也非None
      if(curNode != None):
         while(curNode.subject != None):
            print(format(curNode.value, '<4d'), end = '')
            curNode = curNode.subject
            fields += 1
         fields += 1
         print(curNode.value) #最後一個節點
         print('走訪', fields, '節點')
      else:
         print('空白的節點')

#產生Score物件 chin, eng, math, ds
grade = [78, 96, 65, 82] #List物件
ds = Score(grade[3], None)
math = Score(grade[2], ds)
eng = Score(grade[1], math)
chin = Score(grade[0], eng)
headNode = chin
chin.TraversingNodes()
