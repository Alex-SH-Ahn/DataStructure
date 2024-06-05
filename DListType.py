class DListNode:
  def __init__(self, data, prev, next):
    self.data = data
    self.prev = prev
    self.next = next

class DListType:
  #! head가 됐던, tail이 됐던 하나는 있어야함
  #! head pointer가 있으면 시작부터 끝까지 확인 가능
  #! tail pointer가 있으면 끝부터 시작까지 확인 가능 -> head, tail pointer 모두 존재하는게 효율적
  def __init__(self):
    self.front = self.rear = None
    self.size = 0
    
  def addFront(self, data):
    node = DListNode(data, None, self.front) #* 구슬을 손에 쥐기
    #* 새로 들어가는 노드가 기존의 front를 next로 가지게 됨
    
    if self.size == 0: #* isEmpty() 대신 size로 확인
      self.front = self.rear = node
    else: #* 하나라도 다른 노드가 존재했다면
      self.front.prev = node
      self.front = node
    self.size += 1
  
  def addRear(self, data):
    #? 내가 작성한 코드
    node = DListNode(data, self.rear, None)
    
    if self.size == 0:
      self.rear = self.front = node
    else:
      self.rear.next = node #* rear의 next는 새로운 노드
      self.rear = node #* rear가 새로운 노드를 가리킴
    self.size += 1
    
    #? 정답 코드
    # node = DListType(data, self.rear, None)
    # if self.size == 0:
    #   self.rear = self.front = node
    # else:
    #   self.rear.next = node
    #   self.rear = node
    # self.size += 1
  
  def addPos(self, pos, data):
    node = DListNode(data, None, None)
    
    if pos == 1: #* 맨 앞을 가리킬때
      self.addFront(data)
    elif pos == self.size + 1: #* 맨 끝을 가리킬때
      self.addRear(data)
    else:
      p = self.front
      for i in range(1, pos):
        #* p는 내가 추가하고 싶은 위치의 그 다음 노드
        p = p.next
      node.prev = p.prev
      node.next = p
      p.prev.next = node
      p.prev = node
      self.size += 1
  
  def deletePos(self, pos):
    if pos < 1 or pos > self.size:
      print('Invalid position')
    elif pos == 1:
      self.deleteFront()
    elif pos == self.size:
      self.deleteRear()
    else:
      p = self.front
      for i in range(1, pos):
        p = p.next #* p는 내가 추가하고 싶은 위치의 그 다음 노드
      p.prev.next = p.next
      p.next.prev = p.prev
      self.size -= 1
    
  def deleteFront(self):
    if self.size != 0:
      data = self.front.data
      self.front = self.front.next
      
      if self.front == None: #* 노드가 하나였을때 self.front가 None이 됨
        self.rear = None #* 노드가 하나도 남아있지 않으므로 rear도 None
        # self.rear가 유령값 갖는 것 방지
      else:
        self.front.prev = None #* 새로운 노드의 prev가 None이 됨
      self.size -= 1
      return data
    
  def deleteRear(self):
    if self.size != 0:
      data = self.rear.data
      self.rear = self.rear.prev
      
      if self.rear == None:
        self.front = None
      else:
        self.rear.next = None
      self.size -= 1
      return data
    
  def display(self):
    #! displayPrev, displayNext 등 사용해서 앞부터 보여주기, 뒤부터 보여주기 함수 작성 가능
    p = self.front
    
    while p != None:
      print('[%c] <-> ' % p.data, end='')
      p = p.next
    print('\b\b\b\b    ') #* 마지막에 출력되는 화살표를 지워주는 코드(backspace)
    
if __name__ == '__main__':
  DL = DListType()
  
  DL.addRear('A'); DL.addFront('B'); DL.display();
  DL.addFront('C'); DL.addRear('D'); DL.display();
  DL.addPos(3, 'E'); DL.display();
  
  print('[%c] is deleted :' % DL.deleteFront(), end=''); DL.display();
  