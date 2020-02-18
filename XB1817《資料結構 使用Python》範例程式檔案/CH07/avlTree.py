class Node:
   def __init__(self, data, balance, left, right):
      self.data = data
      self.balance = 0
      self.left = left
      self.right = right

class AVLTree:
   def __init__(self):
      self.root = None

   def inOrder(self):   #中序走訪
      self.inOrderTo(self.root)

   def inOrderTo(self, base):
      if base != None:
         self.inOrderTo(base.left)
         print(base.data, end = ' ')
         self.inOrderTo(base.right)

   def insert(self, data):
      node = Node(data, 0, None, None)
      [self.root, taller] = self.insertAVLTo(
            self.root, node)

   def insertAVLTo(self, base, node):
      if base == None:
         base = node #作為根節點
         base.balance = 0 #平衡系數為0
         taller = True
      #節點的值 < 根節點的值, 新值加到左子樹
      elif node.data < base.data:
         [base.left, taller] = self.insertAVLTo(
               base.left, node)
         if taller:
            if base.balance == 0 :
               base.balance = -1
            elif base.balance == 1:
               base.balance = 0
               taller = False
            else:
               base = self.rightLeftRotate(base)
               taller = False
      else : #節點的值 > 根節點的值, 新值加到右子樹
         [base.right, taller] = self.insertAVLTo(
               base.right, node)
         if taller: #查看平衡係數
            if base.balance == -1:
               base.balance = 0
               taller = False
            elif base.balance == 0 :
               base.balance = 1
            else:   
               base = self.rightLeftRotate(base) 
               taller = False
      return [base, taller]

   def rightLeftRotate2(self, root):
      X = root.right
      if X.balance == 1:
         root.balance = 0
         X.balance = 0
         root = self.singleRightRoate(r)
      else:
         Y = X.left
         if Y.balance == -1:
            root.balance = 0 
            X.balance = 1
         elif Y.balance == 0:
            root.balance = 0
            X.balance = 0
         else:
            root.balance = -1
            X.balance = 0
         Y.balance = 0
         root.right = self.singleLeftRotate(X)
         root = self.singleRightRoate(root)
      return root

   def rightLeftRotate(self, root): #LR、RL型旋轉
      X = root.left
      if X.balance == -1:
         root.balance = 0
         X.balance = 0
         root = self.singleLeftRotate(root)
      else:
         Y = X.right
         if Y.balance == -1:
            root.balance = 1
            X.balance = 0
         elif Y.balance == 0:
            root.balance = 0
            X.balance = 0 
         else:
            root.balance = 0
            X.balance = -1
            Y.balance = 0
            root.left = self.singleRightRoate(X)
            root = self.singleLeftRotate(root)
      return root

   def rightRotate(self, pivot): #RR型旋轉
      child = pivot.right
      pivot.right = child.left
      child.left = pivot
      return child

   def leftRotate(self, pivot): #LL型旋轉
      child = pivot.left
      pivot.left = child.right
      child.right = pivot
      return child

   def height(self): #取得樹高
      return self.updateHt(self.root)
          
   def updateHt(self, root): #更新樹高
      if root == None:
         return 0
      else:
         leftH = self.updateHt(root.left)
         rightH = self.updateHt(root.right)
         if leftH > rightH:
            return 1 + leftH
         else:
            return 1 + rightH

def main():
   avl = AVLTree()
   data = [64, 25, 118, 17, 35, 84, 21, 154]
   for k in range(len(data)):
      avl.insert(data[k])
   avl.insert(31)
   avl.leftRotate(avl.root)
   avl.inOrder()
   print('\n樹高 = ', avl.height())

if __name__ == '__main__':
    main()