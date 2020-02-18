#使用dict()建構函式轉換為字典物件
vertex = dict()
vertex['A'] = ['B', 'C', 'D', 'E']
vertex['B'] = ['A', 'D']
vertex['C'] = ['A', 'E']
vertex['D'] = ['B', 'B', 'E']
vertex['E'] = ['A', 'C', 'D']

# 以key輸出字典及key所對應的value
for key in vertex: #讀取字典
   print(key, vertex[key])
   
#呼叫BIF的sorted將字典物件的key排序
itemMx = sorted(vertex.keys())

#取得矩陣的列、欄的長度
cols = rows = len(itemMx)

#依讀取的列、欄數以二維List生成式來產生相鄰矩陣
matrixes = [[0 for x in range(rows)] for y in range(cols)]
graph = [] #儲存含有邊線的圖形，它會帶出兩端的頂點

#使用雙層for廻圈依據經由排序過的key新增項目
for key in itemMx:
   for neighbor in vertex[key]:
      graph.append((key, neighbor))

#將被標記的邊以1來填滿
for edge in graph:
   indexZero = itemMx.index(edge[0])
   indexOne = itemMx.index(edge[1])
   matrixes[indexZero][indexOne] = 1
   print(edge, end = ' ')