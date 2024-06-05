# Heap or Priority Queue(Q)

N = 100

class MaxHeap: #! MinHeap으로 만들고 싶으면 크기비교만 바꿔주면 됨
  def __init__(self):
    self.heap = [None] * N
    self.heapSize = 0

  def upHeap(self):
    i = self.heapSize #* 마지막 인덱스를 저장: i <- 11
    item = self.heap[i] #* 새로 들어온 값: item <- 8
    
    #* i == 1이면 루트노드임 -> 더이상 올라갈 곳이 없음
    #* 1이 아니라면 부모노드가 있음 = 비교할 값이 있음
    while (i != 1) and (item > self.heap[i // 2]):
      self.heap[i] = self.heap[i // 2] #* H[11] <- 4, H[5] <- 7
      i = i // 2 #* i <- 5, 2

    self.heap[i] = item #* H[2] <- 8
    
  def downHeap(self):
    item = self.heap[1] #* item <- 3
    parent = 1 #* upHeap에서는 i의 역할을 했음
    child = 2 #* 왼쪽자식이 먼저니까 (H[2])
    
    while child <= self.heapSize: #* 2 <= 10 ? 있다면 자식이 있다는 것 = 비교해야할 노드가 있다는 것
      #! 한번 더 생각해보기 이해안됨
      if (child < self.heapSize) and (self.heap[child+1] > self.heap[child]):
        #* 오른쪽 자식도 있어 ? 비교할 자식이 한 명이나 두 명이냐를 확인 and 형제 노드끼리 비교 -> 그 형제가 더 큰 값이면
        child += 1 #* 비교할 자식은 그 형제가 됨
      
      if item >= self.heap[child]:
        break #* 반복(비교)을 할 필요가 없으므로
      
      self.heap[parent] = self.heap[child]
      parent = child
      child *= 2
        
    self.heap[parent] = item
    
  def insertItem(self, item):
    self.heapSize += 1
    self.heap[self.heapSize] = item #* 완전이진트리의 규칙을 따름
    self.upHeap()
    
  def removeItem(self): #* 삭제연산: 우선순위 큐 !루트노드만 삭제 가능
    #! 자료구조에서 삭제되는 아이템은 항상 반환해야함!!! -> 저장 필수
    item = self.heap[1] # item <- 9
    self.heap[1] = self.heap[self.heapSize] #* H[1] <- H[11]
    self.heapSize -= 1
    self.downHeap()
    
    return item
    
if __name__ == "__main__":
  H = MaxHeap()
  data = [7, 3, 5, 6, 4, 9, 2, 3, 1, 2]
  
  for e in data:
    H.insertItem(e)
    print('Heap :', H.heap[1:H.heapSize+1])
  print() 
  
  print('[%d] is deleted' % H.removeItem())
  print('Heap removed :', H.heap[1:H.heapSize+1])
  print()
  print('[%d] is deleted' % H.removeItem())
  print('Heap removed :', H.heap[1:H.heapSize+1])
  
  H.insertItem(8)
  print('\nHeap with 8 :', H.heap[1:H.heapSize+1])