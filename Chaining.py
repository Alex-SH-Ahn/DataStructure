class Node:
  def __init__(self, data, next = None):
    self.data = data
    self.next = next

M = 13 # 헤드포인터를 배열로 만드는 것: 방번호를 배열로 만들기

class HashTable:
  def __init__(self):
    self.table = [None] * M
  
  def hashFn(self, key):
    return key % M
  
  def insert(self, key):
    b = self.hashFn(key) # 버킷번호 받기
    node = Node(key)
    node.next = self.table[b] #? insertFirst()
    self.table[b] = node
  
  def display(self):
    for i in range(M):
      print('Hash Table[%02d] : ' % i, end='')
      n = self.table[i]
      if n == None:
        print()
      else:
        while n is not None:
          print(n.data, end=' ') #* 다음노드 출력
          n = n.next
        print()

if __name__ == "__main__":
  import random
  
  HT = HashTable()
  
  for i in range(10):
    HT.insert(random.randint(0, 10))
  
  HT.display()