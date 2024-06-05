# Cheat Sheet
#* -------------연결된 스택-------------
class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class LinkedStack:
  def __init__(self):
    self.top = None
    self.size = 0
  
  def isEmpty(self): return self.top == None
  def clear(self): self.top = None
  
  def push(self, data):
    node = Node(data, self.top)
    self.top = node
    self.size += 1
  
  def pop(self):
    if not self.isEmpty():
      p = self.top
      data = p.data
      self.top = p.next
      self.size -= 1
      return data
    else:
      print("Stack is Empty")

  def peek(self):
    if not self.isEmpty():
      print(self.top.data)
    else:
      print("Stack is Empty")

  def display(self):
    p = self.top
    while p != None:
      print('[%s] -> ' % p.data)
      p = p.next
    print('\b\b\b\b   ')

#* ------------연결 리스트--------------

class LinkedList:
  def __init__(self):
    self.head = None
    self.size = 0
  
  def isEmpty(self): return self.head == None
  
  def getNode(self, pos): # 포지션의 노드를 찾아줌
    p = self.head
    if pos == 1: return None
    else:
      while pos > 2:
        p = p.next
        pos -= 1
      return 0

  def getEntry(self, pos): # 포지션 앞 노드의 값 반환
    node = self.getNode(pos)
    if node == None: return None
    else: return node.data
  
  def insert(self, pos, data):
    before = self.getNode(pos)
    if before == None:
      self.head = Node(data, self.head)
    else:
      node = Node(data, before.next)
      before.next = node
    self.size += 1
  
  def delete(self, pos):
    before = self.getNode(pos)
    
    if before == None:
      if not self.isEmpty():
        self.head = self.head.next
    else:
      before.next = before.next.next
    self.size -= 1
  
  def display(self):
    p = self.head
    
    while p != None:
      print('[%s] -> ' % p.data, end='')
      p = p.next
    print('\b\b\b\b     ')

#* --------------정렬-------------------

def printStep(A, index):
  print('Step %d : ' % index, end='')
  print(A)

def selectionSort(A): #? 선택정렬
  n = len(A)
  
  for i in range(n-1):
    least = i
    for j in range(i+1, n):
      if A[j] < A[least]:
        least = j
    A[i], A[least] = A[least], A[j]
    printStep(A, i+1)

def insertionSort(A): #? 삽입정렬
  n = len(A)
  
  for i in range(1, n):
    key = A[i]
    j = i - 1
    while j >= 0 and A[j] > key:
      A[j+1] = A[j]
      j -= 1
    A[j+1] = key
    printStep(A, i)

def bubbleSort(A): #? 버블정렬
  n = len(A)
  
  for i in range(n-1, 0, -1):
    bChanged = False
    for j in range(i):
      if (A[j] > A[j+1]):
        A[j], A[j+1] = A[j+1], A[j]
        bChanged = True
    if not bChanged: break
    printStep(A, n-1)

#* --------------이진탐색-----------------

def rBinarySearch(A, key, low, high):
  if low > high:
    return -1
  
  mid = (low, high) // 2
  print(A[mid], end=' ')
  
  if A[mid] == key:
    return mid
  elif key < A[mid]:
    return rBinarySearch(A, key, low, mid - 1)
  else:
    return rBinarySearch(A, key, mid + 1, high)

def iBinarySearch(A, key):
  low = 0
  high = len(A)
  
  while (low <= high):
    mid = (low + high) // 2
    print(A[mid], end=' ')
    
    if key == A[mid]:
      return mid
    elif key < A[mid]:
      high = mid - 1
    else:
      low = mid
  return -1

#* ------------해싱의 오버플로 해결 방법-----------
#* 개방 주소법 - 선형조사법, 이차조사법, 이중해싱법

M = 13
table = [0] * M

def hashFn(key):
  return key % M

def hashFn2(key): # 이중해싱법을 위한 새로운 해시함수
  return 11 - (key % 11)

def getLinear(v, i): # 선형 조사법
  return (v + i) % M

def getQuadratic(v, i): # 이차 조사법
  return (v + i * i)  % M

def getDoubleHashing(v, i, key):
  return (v + i * hashFn2(key)) % M

def insert(key):
  v = hashFn(key)
  i = 0 # 탐색횟수
  
  while i < M:
    b = getLinear(v, i)
    b = getQuadratic(v, i)
    b = getDoubleHashing(v, i, key)
    
    if table[b] == 0:
      table[b] = key
      return
    else:
      i += 1

def search(key):
  v = hashFn(key)
  i = 0
  
  while i < M:
    b = getLinear(v, i)
    b = getQuadratic(v, i)
    b = getDoubleHashing(v, i, key)
    
    print('[%d] ' % table[b], end='')
    
    if table[b] == 0:
      return 0
    elif table[b] == key: # 내가 찾던 값
      return b # 방번호 반환
    else:
      i += 1
  return 0

def delete(key):
  v = hashFn(key)
  i = 0
  
  while i < M:
    b = getLinear(v, i)
    b = getQuadratic(v, i)
    b = getDoubleHashing(v, i, key)
    
    print('[%d] ' % table[b], end='')
    
    if table[b] == 0:
      print('No key to delete')
      return
    elif table[b] == key: # 내가 찾던 값
      table[b] = -1 # 방번호 반환
    else:
      i += 1
  return 0

def display():
  print()
  print('Bucket           key')
  print('====================')
  
  for i in range(M):
    print('HashTable[%2d] : %2d' % (i, table[i]))

#* 체이닝: 1개 주소 여러개 방

class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class HashTable:
  def __init__(self):
    self.table = [None] * M
  
  def hashFn(self, key):
    return key % M
  
  def insert(self, key):
    b = self.hashFn(key)
    node = Node(key)
    node.next = self.table[b]
    self.table[b] = node
    
  def search(self, key):
    b = self.hashFn(key)
    node = self.table[b]
    while node is not None:
      if node.data == key:
        return b
      node = node.next
    return -1
  
  def delete(self, key):
    b = self.hashFn(key)
    if self.table[b] is None:
      return -1
    if self.table[b].data == key:
      self.table[b] = self.table[b].next
      return
    prev = self.table[b]
    node = prev.next
    while node is not None:
      if node.data == key:
        prev.next = node.next
        return
      prev = node
      node = node.next
    return -1

  def display(self):
    for i in range(M):
      print('Hash Table[%02d] : ' % i, end='')
      n = self.table[i]
      if n == None:
        print()
      else:
        while n is not None:
          print(n.data, end=' ')
          n = n.next
        print()

#* --------------이진트리-----------------

