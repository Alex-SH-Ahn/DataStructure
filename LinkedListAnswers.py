class Node: #! 피피티 기반 작성
  def __init__(self, data, next=None):
    self.data = data
    self.next = next
    
class LinkedList:
  def __init__(self):
    self.head = None
    self.size = 0
  
  def isEmpty(self):  return self.head == None
  
  def getNode(self, pos): #* 포지션의 노드를 찾아줌
    if pos < 0: return None
    node = self.head
    while pos > 0 and node != None:
      node = node.next
      pos -= 1
    return node
  
    """
    p = self.head
    if pos == 1: return None
    else:
      while pos > 2:
        p = p.next
        pos -= 1
      return p
    """
  
  def getEntry(self, pos): #* 포지션 앞 노드의 값을 반환
    node = self.getNode(pos)
    if node == None: return None
    else: return node.data

  def insert(self, pos, data):
    before = self.getNode(pos - 1)
    if before == None:
      self.head = Node(data, self.head)
    else:
      node = Node(data, before.next)
      before.next = node
    self.size += 1
  
  def delete(self, pos):
    before = self.getNode(pos - 1)
    if before == None:
      if self.head != None:
        self.head = self.head.next
    elif before.next != None:
      before.next = before.next.next
    self.size -= 1
  
  def display(self):
    p = self.head

    while p != None:
      print('[%s] -> ' % p.data, end="")
      p = p.next
    print('\b\b\b\b    ')

if __name__ == "__main__":
    L = LinkedList()

    L.insert(1, 'A')
    L.insert(1, 'B')
    L.insert(3, 'C')
    L.display()

    L.delete(2)
    L.display()