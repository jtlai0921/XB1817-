import heapq 

def heapqPush():
    color = []
    #呼叫heappush()方法將color的元素壓入，再以heappop()方法彈出優先佇列最小者
    heapq.heappush(color, (11, 'Red'))
    heapq.heappush(color, (7, 'Green'))
    heapq.heappush(color, (8, 'Blue'))
    print('項目最小者：', heapq.heappop(color))

def heapqLarge():
   student = []
   heapq.heappush(student, (95, 'Tom'))
   heapq.heappush(student, (78, 'Eric'))
   heapq.heappush(student, (67, 'five'))
   heapq.heappush(student, (84, 'Peter'))
   heapq.heappush(student, (67, 'Monica'))
   print('分數最高者：', heapq.nlargest(1, student))
   print('分數最低者：', heapq.nsmallest(1, student))

def heapqSmall():
   word = []
   heapq.heappush(word, (1, 'Large'))
   heapq.heappush(word, (2, 'Middle'))
   print('變更前：', word)
   print('替換：', heapq.heapreplace(word, (1, 'Big')))
   print('變更後：', word)

heapqPush()
heapqLarge()
heapqSmall()
