class Node: #以鏈結串列產生節點
   def __init__(self, value = None):
      self.value = value
      self.right = None #右子節點
      self.left = None  #左子節點
      self.parent = None #父節點

class bsTree: #建立二元搜尋樹的類別
   def __init__(self): #設根節點為None
      self.root = None

   def find(self, value):
      #依輸入值來指定其節點並進一步呼叫findTo()方法
      if self.root is not None:
         return self.findTo(value, self.root)
      else:
         return None

   def findTo(self, value, current):
      # 判斷新節點是否等於、大於、或小於目前節點
      if value == current.value:
         return current
      # 大於目前節點就設為右子節點，大於目前節點就設更為左子節點
      elif value > current.value and current.right != None:
         return self.findTo(value, current.right)
      elif value < current.value and current.left != None:
         return self.findTo(value, current.left)

   def insert(self, value):
      # 插入新節點前先確認根節點是否存在
      if self.root is None:
         self.root = Node(value)
      else:
         self.addTo(value, self.root)

   def addTo(self, value, current):
      # 欲插入的新節點和目前節點做比較
      if value < current.value:
         # 小於目前節點就設為左子節點
         if current.left is None:
            current.left = Node(value)
            current.left.parent = current
         else:
            self.addTo(value, current.left)
      # 大於目前節點的值就設成右子節點
      elif value > current.value:
         if current.right is None:
            current.right = Node(value)
            current.right.parent = current
         else:
            self.addTo(value, current.right)
      else:
         print('樹中已有此值')

   def remove(self, value):
      return self.deleteTo(self.find(value))

   def deleteTo(self, Node):
      #回傳節點中的最小值
      def minimum(tmp):
         current = tmp
         while current.left != None:
            current = current.left
         return current
      # 回傳特殊節點的子節點數
      def childNum(tmp):
         childNum = 0
         if tmp.left != None: childNum += 1
         if tmp.right != None: childNum += 1
         return childNum
      # 取得父節點並刪除，kid儲存子節點數
      genitor = Node.parent
      kid = childNum(Node)
      #1--樹葉節點則無左、右無子節點能直接刪除
      if kid == 0:
         # 自父節點移除節點的參考
         if genitor.left == Node:
            genitor.left = None
         else:
            genitor.right = None
      #2--只有一個子節點，表示它有後代
      elif kid == 1:
         #左子節點不是空的情形下，取得左或右子節點
         if Node.left != None:
            child = Node.left
         else:
            child = Node.right
         #將後代取代為已刪除的子節點
         if genitor.left == Node:
            genitor.left = child
         else:
            genitor.right = child
         child.parent = genitor
      #3--有左、右兩個子節點，變數successor為中序前繼者
      elif kid == 2:
         successor = minimum(Node.right)
         #先複製中序前斷者和欲刪除節點的值再互換，最後才刪除節點
         Node.value = successor.value
         self.deleteTo(successor)

   def search(self, value):
      # 先確認欲搜尋的節點值已經存在，呼叫searchTo()方法
      if self.root is not None:
         return self.searchTo(value, self.root)

   def searchTo(self, value, current):
      # 有此節點回傳True，無此節點回傳False
      #print(value, current.value)
      if value == current.value:
         return str('\n有節點 {}'.format(value))
      elif value < current.value and current.left != None:
         return self.searchTo(value, current.left)
      elif value > current.value and current.right != None:         
         return self.searchTo(value, current.right)
      return str('無此節點')

   def show(self):
      # 輸出節點 - 確認有根節點
      if self.root is not None:
         self.showTree(self.root)

   def showTree(self, current):
      #目前節點非空節點，分別輸出左、右節點的值
      if current is not None:
         self.showTree(current.left)
         print(str(current.value), end = ' ')
         self.showTree(current.right)

bst = bsTree() #產生二元樹物件
bst.insert(60) #插入新節點為根節點
bst.insert(25)
bst.insert(93)
bst.insert(34)
bst.insert(18)
bst.insert(79)
bst.show() #輸出節點

print(bst.search(18))

bst.remove(25) #移除節點
print('刪除一個節點')
bst.show()