import queue

class TreeNode:
  def __init__(self, data, left, right):
    self.data = data
    self.left = left
    self.right = right
    
class BinaryTree:
  def __init__(self):
    self.root = None #* 공집합 트리부터 시작
  
  def preOrder(self, node): #! 왼쪽 -> 오른쪽 방문 순서는 바꿀 수 없음
    if node != None:
      print('[%c] ' % node.data, end='') #* 방문한 노드의 값 출력
      self.preOrder(node.left) #* 왼쪽 방문
      self.preOrder(node.right) #* 오른쪽 방문
      
  def inOrder(self, node): 
    if node != None:
      self.inOrder(node.left) #* 왼쪽 방문
      print('[%c] ' % node.data, end='') #* 방문한 노드의 값 출력
      self.inOrder(node.right) #* 오른쪽 방문
      
  def postOrder(self, node): #! 왼쪽 -> 오른쪽 방문 순서는 바꿀 수 없음
    if node != None:
      self.postOrder(node.left) #* 왼쪽 방문
      self.postOrder(node.right) #* 오른쪽 방문
      print('[%c] ' % node.data, end='') #* 방문한 노드의 값 출력
  
  def levelOrder(self, node): #? 레벨 순회
    Q = queue.Queue()
    Q.put(node) #* 1. root node 넣기
    
    while not Q.empty():
      node = Q.get() #* 2. 맨 앞을 가져오기
      print('[%c] ' % node.data, end='') #* 꺼낸 노드의 값 출력
      
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
    return node.left == None and node.right == None #* 왼쪽 자식도 오른쪽 자식도 없으면 외부노드
  
  def getLeafCount(self, node): #* 계층 순서
    count = 0
    if node != None:
      if self.isExternal(node):
        return 1
      else:
        count = self.getLeafCount(node.left) + self.getLeafCount(node.right)
    return count
  
  #! 이 재귀호출이 가장 중요!! 꼭 혼자 해보기
  def getHeight(self, node):
    if node == None:
      return 0
    
    return max(self.getHeight(node.left), self.getHeight(node.right)) + 1
  
  #! 모스 코드 프로그램 꼭 한번 만들어보기

if __name__ == '__main__':
  T = BinaryTree()
  
  #* 여섯개의 노드
  N4 = TreeNode('D', None, None)
  N5 = TreeNode('E', None, None)
  N6 = TreeNode('F', None, None)
  N2 = TreeNode('B', N4, N5)
  N3 = TreeNode('C', N6, None)
  N1 = TreeNode('A', N2, N3)
  
  print('Pre : ', end=''); T.preOrder(N1); print();
  print('In : ', end=''); T.inOrder(N1); print();
  print('Post : ', end=''); T.postOrder(N1); print();
  print('Level : ', end=''); T.levelOrder(N1); print();
  
  print('Num of Nodes : %d' % T.getNodeCount(N1))
  
  print('Num of Leaves : %d' % T.getLeafCount(N1))
  
  print('Height of Tree : %d' % T.getHeight(N1))