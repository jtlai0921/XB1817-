def bitTree(rt):
    return [rt, [None], [None]]

def setRoot(rt, value):
    rt[0] = value #設定根節點的值
def getRoot(rt):
    return rt[0] #回傳根節點的值

def leftChild(rt):
    return rt[1] #回傳左子樹的值
def rightChild(rt):
    return rt[2] #回傳右子樹的值

def insertLeft(rt, item):
    tmp = rt.pop(1)
    #判斷tmp的長度是否大於1
    if len(tmp) > 1:
        rt.insert(1, [item, tmp, [None]]) #依據指定位置插入項目
    else:
        rt.insert(1, [item, [None], [None]])
    return rt

def insertRight(rt, item):
    tmp = rt.pop(2)
    #判斷tmp的長度是否大於1
    if len(tmp) > 1:
        rt.insert(2, [item, tmp, [None]]) #依據指定位置插入項目
    else:
        rt.insert(2, [item, [None], [None]])
    return rt

bt = bitTree('A')
insertLeft(bt, 'D')
insertLeft(bt, 'B')
insertRight(bt, 'F')
insertRight(bt, 'C')
left = leftChild(bt)
right = rightChild(bt)
tree = getRoot(bt)
print(bt)