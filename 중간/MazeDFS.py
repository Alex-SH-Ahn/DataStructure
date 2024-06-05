from ArrayStack import ArrayStack

map = [
  ['1', '1', '1', '1', '1', '1'],
  ['e', '0', '0', '0', '0', '1'],
  ['1', '0', '1', '0', '1', '1'],
  ['1', '1', '1', '0', '0', 'x'],
  ['1', '1', '1', '0', '1', '1'],
  ['1', '1', '1', '1', '1', '1'],
]

class ArrayStackforDFS(ArrayStack):
  def display(self):
    print(self.stack[self.top::-1]) # 맨 위에 있는 것부터 출력

SIZE = 6

# 항상 행이 먼저 나옴
# 행: row, 열: column
def isValidPos(r, c):
  if (0 <= r < SIZE and 0 <= c < SIZE): # SIZE 안에 있는지
    if map[r][c] == '0' or map[r][c] == 'x': # 0이나 x이면 갈 수 있음
      return True
  return False

def DFS():
  print('DFS : ')
  S = ArrayStackforDFS(100) # 100개까지 들어가는 스택 생성
  S.push((1, 0)) # 시작점 -> 스택에 (1,0)이 들어감

  while not S.isEmpty():
    pos = S.pop() # 스택에서 (1,0) 꺼냄
    print(pos, end=' -> ') #현재 상황 출력
    (r, c) = pos # pos를 (r, c)의 형태로 기억시킴

    if (map[r][c]) == 'x':
      return True # 도착점에 도착했을 때 True 반환
    else:
      map[r][c] = '.' # 방문한 곳은 .으로 표시
      if isValidPos(r-1, c): S.push((r-1, c)) # (상 하 좌 우) 순서로 갈 수 있는 곳 탐색
      if isValidPos(r+1, c): S.push((r+1, c))
      if isValidPos(r, c-1): S.push((r, c-1))
      if isValidPos(r, c+1): S.push((r, c+1))
    S.display() # 현재 스택 상태 출력
  return False # 도착점에 도착하지 못했을 때 False 반환

if __name__ == "__main__":
  result = DFS()
  if result:
    print(' --> Success')
  else:
    print(' --> Failed')