class Node: #以鏈結串列產生節點
   def __init__(self, value = None):
      self.value = value
      self.right = None #右子節點
      self.left = None  #左子節點
      self.parent = None #父節點

class bsTree: #建立二元搜尋樹的類別
   def __init__(self): #設根節點為None
      self.root = None

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

   def minumum(self, current):
      current = self.root
      while current.left:
         current = current.left
      return current.value

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
data = [63, 24, 90, 37, 12, 84, 41, 29, 23, 103, 7, 71]
for item in data:
   bst.insert(item)
bst.show()

print('\n最小值', bst.minumum(0))