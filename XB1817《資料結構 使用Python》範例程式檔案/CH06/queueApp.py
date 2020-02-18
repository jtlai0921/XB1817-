from random import randint
import time

class Node:
   '''定義雙向鏈結串列'''
   def __init__(self, data = None, Rnext = None, Lnext = None):
      self.data = data
      self.Rnext = Rnext
      self.Lnext = Lnext

class Queue:
   '''以雙向鏈結實作佇列'''
   def __init__(self):
      self.front = None
      self.rear = None
      self.count = 0

   def enqueue(self, data):
      '''新增項目'''
      newNode = Node(data, None, None)
      #有首節點的情形下，從後端加入新節點
      if self.front is None:
         self.front = newNode
         self.rear = self.front
      else:
         #新節點的左指標指向尾節點
         newNode.Lnext = self.rear
         #尾節點的右指標指向新節點
         self.rear.Rnext = newNode
         #新節點變成最後一個節點
         self.rear = newNode
      self.count += 1

   def dequeue(self):
      '''刪除項目 '''
      current = self.front
      #如果count為1，表示沒有項目
      if self.count == 1:
         self.count -= 1
         self.front = None
         self.rear = None
         #有曲目正在播放，front指標指向正播放曲目的下一首
      elif self.count > 1:
         self.front = self.front.Rnext
         self.front.Lnext = None
         self.count -= 1
      return current

play = Queue()#建立佇列物件
start = time.time() #開始時間
#加入或移除播放曲目
for one in range(100000):
    play.enqueue(one)
for one in range(100000):
    play.dequeue()
print('{} 秒'.format(time.time() - start))

class MediaPlayer(Queue):
   '''播放器，繼承了Queue類別'''
   def __init__(self):
     #以super()呼叫父類別
      super(MediaPlayer, self).__init__()

   def addSong(self, song):#呼叫佇列的enqueue()方法新增曲目
      self.enqueue(song)

   def show(self): #播放曲目就呼叫dequeue()方法刪除播放完的曲目
      while self.count > 0:
         cur_song = self.dequeue()
         num =  randint(1, 10)
         print('正在播放 {:>20} {:2} sec'.format(
               cur_song.data.title, num))
         time.sleep(cur_song.data.sec)

class Song:
   '''模仿播放的曲目，配合random類別做隨機播放'''
   def __init__(self, title = None, sec = 0):
      self.title = title #曲目名稱
      self.sec = randint(1, 10) #曲目長度以秒計算

s1 = Song('Dona Nobis Pacem')
s2 = Song('Familia')
s3 = Song('My One and Only Love')
s4 = Song('The Wexford Carol')
s5 = Song('Concordia')
s6 = Song('Kuai Le')
s7 = Song('My Favorite Things')
singing = [s1, s2, s3, s4, s5, s6, s7]

music = MediaPlayer()
for item in singing:
   music.addSong(item)
music.show()

