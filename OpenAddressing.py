M = 13 #* 슬롯의 개수
table = [0] * M

def hashFn(key):
  return key % M #* 나머지 연산 -> 슬롯의 인덱스 (방번호)

def hashFn2(key): #! 이중 해싱법을 위한 새로운 해시함수
  return 11 - (key % 11)

def getLinear(v, i):
  #* 빈방이면 들어가고 아니면 다음 방 탐색
  return (v + i) % M

def getQuadratic(v, i): #! 이차조사법: i는 조사횟수
  return (v + i * i) % M

def getDoubleHashing(v, i, key): #! 이중해싱법
  return (v + i * hashFn2(key)) % M
  #* 오버플로 발생시, i * 0 -> 그 다음은 i * 1이 되어야함

def insert(key):
  v = hashFn(key)
  i = 0 #* 탐색횟수
  
  while i < M:
    b = getLinear(v, i) #? 기존 방식
    #? b = getQuadratic(v, i) #? 이차조사법으로 버킷번호를 받음
    #? b = getDoubleHashing(v, i, key) #? 이중해싱법으로 버킷번호를 받음
    
    if table[b] == 0: #* 빈방이면
      table[b] = key
      return #* 자리 잡았으니까 끝내기
    else:
      i += 1 #* 다음 방으로 이동

def search(key): #! 탐색함수: 삽입만 빼면 거의 동일
  v = hashFn(key)
  i = 0 #* 탐색횟수
  
  while i < M:
    b = getLinear(v, i) #? 기존 방식
    #? b = getQuadratic(v, i) #? 이차조사법으로 버킷번호를 받음
    #? b = getDoubleHashing(v, i, key) #? 이중해싱법으로 버킷번호를 받음
    
    print('[%d] ' % table[b], end='')
    
    if table[b] == 0: #* 찾은 방이 빈방이면
      return 0 #* 값이 없다는거라 리턴 0
    elif table[b] == key: #* 차있는 방 + 내가 찾던 값
      return b #* 방 번호(버킷번호) 아니면 table[b] 리턴
    else: #* 차있는 방 + 내가 찾던 값 아님
      i += 1 #* 다음 방으로 이동
  return 0 #* while문을 빠져나왔는데 리턴이 되지 않았으면 없다는 것! -> 리턴 0

def delete(key): #! 삭제함수
  v = hashFn(key)
  i = 0 #* 탐색횟수
  
  while i < M:
    b = getLinear(v, i) #? 기존 방식
    #? b = getQuadratic(v, i) #? 이차조사법으로 버킷번호를 받음
    #? b = getDoubleHashing(v, i, key) #? 이중해싱법으로 버킷번호를 받음
    
    print('[%d] ' % table[b], end='') # 조사과정 나열
    
    if table[b] == 0: #* 찾은 방이 빈방이면 삭제할 값이 없음
      print('No key to delete')
      return
    elif table[b] == key: #* 차있는 방 + 내가 찾던 값 --> 삭제!
      # table[b] = 0 #* 삭제: 0으로 하면 오류!!
      table[b] = -1 #* 삭제된 값을 다르게 해야함
      return 
    else: #* 차있는 방 + 내가 찾던 값 아님 --> 
      i += 1 #* 다음 방으로 이동
  return 0 #* while문을 빠져나왔는데 리턴이 되지 않았으면 없다는 것! -> 리턴 0

def display():
  print()
  print('Bucket        Key')
  print('=================')
  
  for i in range(M):
    print('HahTable[%2d] : %2d' % (i, table[i]))

if __name__ == "__main__":
  data = [45, 27, 88, 9, 71, 60, 46, 38, 24]
  
  for d in data:
    print('h(%2d)=%2d' % (d, hashFn(d)), end=' ')
    insert(d)
    print(table) #* 중간과정 출력
    
  display()
  
  print('------------------------------')
  
  print('Search(46) ---> ', search(46)) #! 탐색성공
  print('Search(39) ---> ', search(39)) #! 탐색실패
  # 0번 갔는데 없어, 1번 갔는데 없어, 2번 갔는데 0이야 -> 값이 없다는 것!
  
  print('------------------------------')
  
  delete(60)
  # display() #! 삭제 확인
  # print('Search(60) ---> ', search(60)) #! 삭제확인
  print('\n------------------------------')
  
  print('Search(46) ---> ', search(46)) #? 46를 찾아보기 -> 없다고 나옴..!!
  #? 60이 있을 땐 46까지 계속 다음방을 탐색, 60 삭제 후 0이 나와서 없다고 리턴
  