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

#* ----------단순연결구조 큐-------------

class Node:
  def __init__(self, data, next):
    self.data = data
    self.next = next
  
class LinkedLinearQueue:
  def __init__(self):
    self.front = None
    self.rear = None
    self.size = 0
  
  def isEmpty(self): return (self.rear == None and self.front == None)
  
  def enqueue(self, data): #? 맨 뒤 삽입
    node = Node(data, None)
    if self.isEmpty():
      self.front = node
      self.rear = node
    else:
      self.rear.next = node
      self.rear = node
    self.size += 1
  
  def dequeue(self, data): #? 맨 앞 삽입
    if not self.isEmpty():
      data = self.front.data
      if self.front == self.rear:
        self.front = None
        self.rear = None
        self.size -= 1
        return data
      else:
        self.front = self.front.next
      self.size -= 1
      return data
    else:
      print("Queue is Empty")

#* ----------원형연결구조의 큐-----------

class Node:
  def __init__(self, data, next):
    self.data = data
    self.next = next

class LinkedCircularQueue(Node):
  def __init__(self):
    self.tail = None
    self.size = 0
  
  def isEmpty(self):
    return self.tail == None
  
  def enqueue(self, data): #? addRear
    node = Node(data, None)
    if self.isEmpty():
      node.next = node
      self.tail = node
    else:
      node.next = self.tail.next
      self.tail.next = node
      self.tail = node
    self.size += 1
    
  def dequeue(self, data): #? deleteFront
    if not self.isEmpty():
      p = self.tail
      q = p.next
      data = q.data
      if p == q:
        self.tail = None
      else:
        p.next = q.next
        
      #* data = self.tail.next.data
      #* if self.tail == self.tail.next:
      #*   self.tail = None
      #* else:
      #*   self.tail.next = self.tail.next.next
      self.size -= 1
      return data
    else:
      print("Queue is Empty")

#* --------원형연결리스트 덱-------------

class DListNode:
  def __init__(self, data, prev, next):
    self.data = data
    self.prev = prev
    self.next = next

class DListType:
  def __init__(self):
    self.front = self.rear = None
    self.size = 0
  
  def addFront(self, data):
    node = DListNode(data, None, self.front)
    
    if self.size == 0:
      self.front = self.rear = node
    else:
      self.front.prev = node
      self.front = node
    self.size += 1
  
  def addRear(self, data):
    node = DListNode(data, self.rear, None)
    
    if self.size == 0:
      self.rear = self.front = node
    else:
      self.rear.next = node
      self.rear = node
    self.size += 1
  
  def addPos(self, pos, data):
    node = DListNode(data, None, None)
    
    if pos == 1:
      self.addFront(data)
    elif pos == self.size + 1:
      self.addRear(data)
    else:
      p = self.front
      for i in range(1, pos):
        p = p.next
      node.prev = p.prev
      node.next = p
      p.prev.next = node
      p.prev = node
      self.size += 1

  def deleteFront(self):
    if self.size != 0:
      data = self.front.data
      self.front = self.front.next
      
      if self.front == None:
        self.rear = None
      else:
        self.front.prev = None
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

  def deletePos(self, pos):
    if pos < 1 or pos > self.size:
      print('Invalid Position')
    elif pos == 1:
      self.deleteFront()
    elif pos == self.size:
      self.deleteRear()
    else:
      p = self.front
      for i in range(1, pos):
        p = p.next
      p.prev.next = p.next
      p.next.prev = p.prev
      self.size -= 1

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

def getLinear(v, i): #? 선형 조사법
  return (v + i) % M

def getQuadratic(v, i): #? 이차 조사법
  return (v + i * i)  % M

def getDoubleHashing(v, i, key): #? 이중 해싱법
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

import queue

class Treenode:
  def __init__(self, data, left, right):
    self.data = data
    self.left = left
    self. right = right

class BinaryTree:
  def __init__(self):
    self.root = None
  
  def preOrder(self, node): #? 전위순회
    if node != Node:
      print('[%c] ' % node.data, end='')
      self.preOrder(node.left)
      self.preOrder(node.right)
  
  def inOrder(self, node): #? 중위순회
    if node != None:
      self.inOrder(node.left)
      print('[%c] ' % node.data, end='')
      self.inOrder(node.right)
  
  def postOrder(self, node): #? 후위순회
    if node != None:
      self.postOrder(node.left)
      self.postOrder(node.right)
      print('[%c] ' % node.data, end='')
  
  def levelOrder(self, node): #? 레벨순회
    Q = queue.Queue()
    Q.put(node)
    
    while not Q.empty():
      node = Q.get()
      print('[%c] ' % node.data, end='')
      
      if node.left != None:
        Q.put(node.left)
      
      if node.right != None:
        Q.put(node.right)
  
  def getNodeCount(self, node):
    count = 0
    if node != None:
      count = 1 + self.getNodeCount(node.left) + self.getNodeCount(node.right)
    return count
  
  def isExternal(self, node):
    return node.left == None and node.right == None

  def getLeafCount(self, node):
    count = 0
    if node != None:
      if self.isExternal(node):
        return 1
      else:
        count = self.getLeafCount(node.left) + self.getLeafCount(node.right)
    return count
  
  def getHeight(self, node):
    if node == None:
      return 0
    else:
      left_height = self.getHeight(node.left)
      right_height = self.getHeight(node.right)
      return max(left_height, right_height) + 1
  
#* --------------최대 힙-----------------
# MinHeap 만들고 싶으면 크기비교 바꿔주면 됨
N = 100

class MaxHeap:
  def __init__(self):
    self.heap = [None] * N
    self.heapSize = 0
  
  def upHeap(self):
    i = self.heapSize
    item = self.heap[i]
    
    while (i != 1) and (item > self.heap[i // 2]):
      self.heap[i] = self.heap[i // 2]
      i = i // 2
    
    self.heap[i] = item
  
  def downHeap(self):
    item = self.heap[1]
    parent = 1
    child = 2
    
    while child <= self.heapSize:
      if (child < self.heapSize) and (self.heap[child+1] > self.heap[child]):
        child += 1
      if item >= self.heap[child]:
        break
      self.heap[parent] = self.heap[child]
      parent = child
      child *= 2
      
    self.heap[parent] = item
  
  def insertItem(self, item):
    self.heapSize += 1
    self.heap[self.heapSize] = item
    self.upHeap()
  
  def removeItem(self):
    item = self.heap[1]
    self.heap[1] = self.heap[self.heapSize]
    self.heapSize -= 1
    self.downHeap()
    return item 
  
#* ------------이진탐색트리---------------

class TreeNode:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None
  
def minKeyNode(root):
  while root != None and root.left != None:
    root = root.left
  return root

def delete(root, key):
  if root == None:
    return None
  
  if key < root.key:
    root.left = delete(root.left, key)
  elif key > root.key:
    root.right = delete(root.right, key)
  else:
    if root.left == None:
      return root.right
    elif root.right == None:
      return root.left
    else:
      successor = minKeyNode(root.right)
      root.key = successor.key
      root.right = delete(root.right, successor.key)
  return root

def insert(root, key):
  if root == None:
    return TreeNode(key)
  
  if key > root.key:
    root.left = insert(root.left, key)
  elif key > root.key:
    root.right = insert(root.right, key)
  
  return root

def inOrder(root): #? 중위순회
  if root:
    inOrder(root.left)
    print('%2d ' % root.key, end='')
    inOrder(root.right)

#* ---------그래프 깊이우선전략------------

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

def iDFS(u):
  S = LifoQueue()
  S.put(u)
  
  while not S.empty():
    u = S.get()
    S.put(u)
    
    if visited[u] == False:
      visited[u] = True
      print(Vertex[u], end=' ')
    flag = True
    
    for v in AdjVer[u]:
      if visited[v] == False:
        S.put(v)
        flag = False
        break
    
    if flag == True:
      S.get()

#* ---------그래프 깊이우선전략------------

def rDFS(visited, u):
  visited[u] = True
  print(Vertex[u], end=' ')
  
  for v in AdjVer[u]:
    if visited[v] == False:
      rDFS(visited, v)

visited = [False] * len(Vertex)
print('rDFS(A) : ', end='')
rDFS(visited, 0)

#* --------------KrusKal-----------------

Graph = {'A':[('B', 29), ('F', 10)],
        'B':[('A', 29), ('C', 16), ('G', 15)],
        'C':[('B', 16), ('D', 12)],
        'D':[('C', 12), ('E', 22), ('G', 18)],
        'E':[('D', 22), ('F', 27), ('G', 25)],
        'F':[('A', 10), ('E', 27)],
        'G':[('B', 15), ('D', 18), ('E', 25)]}

vertices = [-1, -1, -1, -1, -1, -1, -1]
eList = []

def edgeSort():
  for v in Graph:
    for e in Graph[v]:
      if v < e[0]:
        eList.append([v, e[0], e[1]])
  eList.sort(key=lambda e : e[2], reverse=True)
  
  for i in range(len(eList)-1, -1, -1):
    print('[%c%c%d] ' % (eList[i][0], eList[i][1], eList[i][2]), end='')
  print(); print()

def find(vNum):
  while vertices[vNum] != -1:
    vNum = vertices[vNum]
  return vNum

def union(vNum1, vNum2):
  vertices[vNum2] = vNum1

def kruskal():
  eCnt = 0
  vCnt = len(Graph)
  
  edgeSort()
  
  while eCnt < vCnt-1:
    e = eList.pop()
    vNum1 = find(ord(e[0])-65)
    vNum2 = find(ord(e[1])-65)
    
    if vNum1 != vNum2:
      eCnt += 1
      print('%d. [%s%s %d]' % (eCnt, e[0], e[1], e[2]))
      union(vNum1, vNum2)

#* ----------------Prim------------------

INF = 100
dist = [INF] * len(Graph)
visited = [False] * len(Graph)

def findMin():
  minDist = INF
  minV = 0
  for v in range(len(dist)):
    if visited[v] == False and dist[v] < minDist:
      minDist = dist[v]
      minV = v
  return minV

def prim(vName):
  vCnt = len(Graph)
  dist[ord(vName)-65] = 0
  
  for i in range(vCnt):
    for j in range(vCnt):
      print('%3d ' % dist[j], end='')
    print()
    
    vNum = findMin()
    vName = chr(vNum+65)
    
    visited[vNum] = True
    #print('[%c(%d)] ' % (vName, dist[vNum]), end='')
    
    for e in Graph[vName]:
      vNum = ord(e[0])-65
      if visited[vNum] == False and e[1] < dist[vNum]:
        dist[vNum] = e[1]