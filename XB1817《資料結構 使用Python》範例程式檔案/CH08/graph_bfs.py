from collections import deque

vertex = dict() #產生字典物件
vertex['A'] = ['B', 'D', 'C']
vertex['B'] = ['A', 'D']
vertex['C'] = ['D', 'A']
vertex['D'] = ['B', 'A', 'C']
vertex['E'] = ['F', 'C']
vertex['F'] = ['E']

def bfSearch(vertex, root):
   visited = list()
   que = deque([root])
   visited.append(root)
   node = root
   while len(que) > 0:
      node = que.popleft()
      neighbor = vertex[node]
      #將集合物件做差集計算-以相鄰頂點為主來產生新集合存放正走訪的頂點
      # attend - 記錄List物件中某一組正在走訪的節點
      attend = set(neighbor) - set(visited)
      #若走訪中頂點的長度大於零，呼叫BIF sorted()函式做排序
      if len(attend) > 0:
         #將已走訪的頂點新增到「已拜訪」List物件中
         for item in sorted(attend):
            visited.append(item)
            que.append(item) #新增元素到佇列
   return visited

print(bfSearch(vertex, 'A'))

