Vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
AdjVer = [[1, 2],
          [0, 3],
          [0, 3, 4],
          [1, 2, 5],
          [2, 6, 7],
          [3],
          [4, 7],
          [4, 6]]

from queue import LifoQueue # Stack
visited = [False] * len(Vertex)

def iDFS(u): # 명시적 스택이면 peek 시점이 중요
  S = LifoQueue()
  S.put(u)
  
  while not S.empty():
    u = S.get()
    S.put(u) # peek()
  
    if visited[u] == False:
      visited[u] = True 
      print(Vertex[u], end=" ")
      
    flag = True # flag variable
    
    for v in AdjVer[u]:
      if visited[v] == False:
        S.put(v) 
        flag = False
        break # 깊이우선을 계속 넣지 않아도됨
      
    if flag == True:
      S.get()

if __name__ == "__main__":
  print('iDFS(A) : ', end='')
  iDFS(0)