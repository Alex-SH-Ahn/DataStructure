from CircularQueue import CircularQueue

class CircularQueueforBFS(CircularQueue):
  def display(self):
    print(self.queue[self.front + 1:self.rear+1]) # 맨 위에 있는 것부터 출력

map = [
  ['1', '1', '1', '1', '1', '1'],
  ['e', '0', '1', '0', '0', '1'],
  ['1', '0', '0', '0', '1', '1'],
  ['1', '0', '1', '0', '1', '1'],
  ['1', '0', '1', '0', '0', 'x'],
  ['1', '1', '1', '1', '1', '1'],
]

SIZE = 6

def isValidPos(r, c):
  if (0 <= r < SIZE and 0 <= c < SIZE): # SIZE 안에 있는지
    if map[r][c] == '0' or map[r][c] == 'x': # 0이나 x이면 갈 수 있음
      return True
  return False

def BFS():
  Q = CircularQueueforBFS(50)
  Q.enqueue((1, 0)) # 시작점 -> 큐에 (1,0)이 들어감
  print('BFS : ')
  
  while not Q.isEmpty():
    pos = Q.dequeue() # 큐에서 (1,0) 꺼냄/현재 포지션 알려줌
    print(pos, end=' -> ')
    (r, c) = pos # pos를 (r, c)의 형태로 기억시킴

    if (map[r][c]) == 'x':
      return True # 도착점에 도착했을 때 True 반환
    else:
      map[r][c] = '.' # 방문한 곳은 .으로 표시
      if isValidPos(r-1, c): Q.enqueue((r-1, c)) # (상 하 좌 우) 순서로 갈 수 있는 곳 탐색
      if isValidPos(r+1, c): Q.enqueue((r+1, c))
      if isValidPos(r, c-1): Q.enqueue((r, c-1))
      if isValidPos(r, c+1): Q.enqueue((r, c+1))
    Q.display() # 현재 큐 상태 출력
  return False # 도착점에 도착하지 못했을 때 False 반환

if __name__ == "__main__":
  result = BFS()
  if result:
    print(' --> Success')
  else:
    print(' --> Failed')