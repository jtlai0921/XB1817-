#使用Doubly Linked List來處理二元樹
class bitTree():
   def __init__(self, root):
      self.left = None #left Node
      self.right = None # right Node
      self.root = root

   def leftChild(self):
      return self.left #回傳left node data

   def rightChild(self):
      return self.right #回傳right node data

   def setRoot(self, data):
      self.root = data #設定根節點新值

   def getRoot(self):
      return self.root #回傳根節點的值

   def insertLeft(self, data):
      #如果左子樹為空樹，取得二元樹的新值
      if self.left == None:
         self.left = bitTree(data)
      else:
         bt = bitTree(data)
         bt.left = self.left #將新節點的值設為自己的左節點
         self.left = bt

   def insertRight(self, data):
      #如果右子樹為空樹，取得二元樹的新節點的值
      if self.right == None:
         self.right = bitTree(data)
      else:
         bt = bitTree(data)
         bt.right = self.right #將目前右節點的預設值設給bt
         self.right = bt #取得二元樹根節點的值

def show(bt):
    if(bt != None):
        show(bt.leftChild())
        print(bt.getRoot(), end = ' ')
        show(bt.rightChild())

bt = bitTree('A')
bt.insertLeft('D')
bt.insertLeft('B')
bt.insertRight('E')
bt.insertRight('C')
show(bt)