#以List實作Priority Queue 不能運作
class PQcolor:
   def __init__(self, elem, prior):
      self.elem = elem
      self.prior = prior

class PriorityQueue :
   '''產生不受限的空白優先佇列'''
   def __init__(self):
     self.Ary = []

   def isEmpty(self): #空白佇列已True回傳
      return len(self) == 0

   def __len__( self ): #取時佇列長度
      return len(self.Ary)

   def enqueue(self, elem, prior): #新增元素
      entry = PQcolor(elem, prior)
      self.Ary.append(entry)
      return self.Ary

   def dequeue(self):  #移除項目
      id =0 #做優先權(權重)比較
      if self.isEmpty() == False:
         #找出優先佇列最高者
         highest = self.Ary[id].prior
         for id in range(len(self)) :
            #小於最高優先權
            if self.Ary[id].prior < highest :
               highest = self.Ary[id].prior
         #移除最高優先權並回傳
         entry = self.Ary.pop(highest)
         print('最大優先權', entry.elem)
         return entry.elem
      else:
         print('空白佇列無法刪除')

color = PriorityQueue()
color.enqueue('Yelloe', 5)
color.enqueue('Blue', 2)
color.enqueue('Green', 3)
color.dequeue()

