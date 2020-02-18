class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

#中序追踪--D->B->E->A->F->C->G
def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.item, end = '-> ')
        inOrder(root.right)

#前序走訪--A->B->D->E->C->F->G
def preOrder(root):
    if root:
        print(root.item, end = '-> ')
        preOrder(root.left)
        preOrder(root.right)

#後序走訪--D->E->B->F->G->C->A
def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.item, end = '-> ')

#產生節點物件
root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.left = Node('F')
root.right.right = Node('G')

inOrder(root)
print()
preOrder(root)
print()
postOrder(root)
