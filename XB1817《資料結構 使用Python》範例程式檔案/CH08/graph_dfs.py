from collections import defaultdict
import sys
import inspect

class Graph:
   def __init__(self, num):
      self.count = num
      self.graph = defaultdict(list)

   def addEdge(self, top, vex):
      self.graph[top].append(vex)

   def bfs(self, start):
      visited = [False] * self.count
      qe = [] #空的List
      qe.append(start)
      visited[start] = True
      print('從 {} 開始, 走訪'.format(start), end = '')
      while(1):
         v = qe.pop(0)
         for node in self.graph[v]:
            if visited[node] == False:
               qe.append(node)
               visited[node] = True
               print(format(node, '2'), end = ' ')
         if len(qe) == 0:
            break

   def dfs(self, start):
      print('以DFS取得堆疊初始化長度', len(inspect.stack()))
      visited = [False] * self.count
      for node in list(range(self.count)):
         if visited[node] == False:
            self.dfsTo(node, visited)

   def dfsTo(self, vex, visited):
      print('堆疊長度', len(inspect.stack()))
      visited[vex] = True
      print(vex, end = ' ')
      for node in self.graph[vex]:
         if visited[node] == False:
            self.dfsTo(node, visited)

gr = Graph(6)
gr.addEdge(0, 1)
gr.addEdge(0, 3)
gr.addEdge(0, 2)
gr.addEdge(2, 4)
gr.addEdge(4, 5)

gr.dfs(0)
print()
for k, v in gr.graph.items():
   print(k,':', v)