import heapq

class PriorityQueue:
   '''產生PriorityQueue類別'''
   def __init__(self):
      self.queue = []
      self.index = 0 #比較優先佇列等級

   def push(self, item, prior):
      '''呼叫heapqpush()函式壓入堆積佇列項目'''
      heapq.heappush(self.queue, (-prior, self.index, item))
      self.index += 1

   def pop(self): #原本heappop()函式彈出最小，負數就變成最大者
      return heapq.heappop(self.queue)[-1]

class Color:   #定義欲實作物件
   def __init__(self, name):
      self.name = name

   def __str__(self):
      return '最大優先權：{}'.format(self.name)

def show():
   ''' 將堆積佇列壓入 '''
   tint = PriorityQueue()
   tint.push(Color('Red'), 3)
   tint.push(Color('Green'), 3)
   tint.push(Color('Blue'), 8)
   tint.push(Color('Yellow'), 12)
   print(tint.pop())

if __name__ == '__main__':
   show()