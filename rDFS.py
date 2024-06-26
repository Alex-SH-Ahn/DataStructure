Vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
AdjVer = [[1, 2],
          [0, 3],
          [0, 3, 4],
          [1, 2, 5],
          [2, 6, 7],
          [3],
          [4, 7],
          [4, 6]]

def rDFS(visited, u): # visited list & starting point
  visited[u] = True
  print(Vertex[u], end=' ')  

  for v in AdjVer[u]:
    if visited[v] == False:
      rDFS(visited, v)

if __name__ == "__main__":
  visited = [False] * len(Vertex) # False * 8
  print('rDFS(A) : ', end='')
  rDFS(visited, 0)