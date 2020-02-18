#以雜湊法做搜尋
class HashItem:
    def __init__(self, key):
        self.key = key

class HashTable:
   def __init__(self):
      '''建立存放鍵值的雜湊表，儲存空間為13'''
      self.size = 13
      self.slots = [None for k in range(self.size)]
      self.count = 0

   def runHash(self, key): #以除法求取餘數
      return key % self.size

   def insert(self, key):
      '''插入新的鍵值：使用線性探測法，找下一個空位'''
      item = HashItem(key)
      addr = self.runHash(key) #算出雜湊位置
      #如果位置不是空的，會發生碰撞
      while self.slots[addr] is not None:
         if self.slots[addr].key is key:
            break
         #使用線性測探法，找出下一個空位插入新值
         addr = (addr + 1) % self.size
      #取得空位插入新值
      if self.slots[addr] is None:
         self.count += 1
         self.slots[addr] = item

   def search(self, key):
      addr = self.runHash(key)
      #print('Addr =', addr)
      while self.slots[addr] is None:
         if key == self.slots[addr]:
            break
         addr = (addr + 1) % self.size
      return addr

htb = HashTable()
data = [7, 35, 311, 46, 313, 51, 31, 614, 335, 613]
for item in data:
   htb.insert(item)
print('Index:', htb.search(35))