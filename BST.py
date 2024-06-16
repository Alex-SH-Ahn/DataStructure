# Binary Search Tree

class TreeNode:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None

def minKeyNode(root):
  while root != None and root.left != None:
    root = root.left #* 왼쪽 끝까지 가기
  return root

def delete(root, key):
  if root == None: 
    return None
  
  if key < root.key: #* 작으면 왼쪽으로
    root.left = delete(root.left, key)
  elif key > root.key: #* 크면 오른쪽으로
    root.right = delete(root.right, key)
  else: #*삭제할 노드 찾음! key == root.key
    if root.left == None: #* 왼쪽 노드가 없음
      return root.right #* 그 전 노드와 root.right를 연결 -> 30의 right는 없음. root[26].right = None 이 됨
    elif root.right == None: #* 왼쪽 노드는 있는데, 오른쪽 노드는 없음
      return root.left
    else: #* 왼쪽 자식이랑 오른쪽 자식 둘 다 있음
    #* 루트노드에 왼쪽과 오른쪽을 둘 다 연결해줘야함(어려움!) => 그 자리에 대체할 값을 덮어씌움 (계승자)
    #* preOrder successor or postOrder successor
    #* 노드를 옮기는 것이 아니라 값을 하나 찾아서 그 값으로 덮어씀 (노드 유지)
      successor = minKeyNode(root.right)
      root.key = successor.key
      root.right = delete(root.right, successor.key)
    
  return root

def insert(root, key):
  if root == None:
    return TreeNode(key)
  
  #* root = 35가 되기 때문에 None이 아님
  if key < root.key: #* 18 < 35 ? 
    root.left = insert(root.left, key)
  elif key > root.key: 
    root.right = insert(root.right, key)
  
  return root

def inOrder(root): #* 중위순회
  if root:
    inOrder(root.left)
    print('%2d ' % root.key, end='')
    inOrder(root.right)

def display(root, msg):
  print(msg, end='')
  inOrder(root)
  print()

if __name__ == '__main__':
  root = None
  data = [35, 18, 7, 26, 3, 22, 30, 12, 26, 68, 99]
  
  for key in data:
    root = insert(root, key) #* root = 35
    display(root, "[Insert %2d] : " % key)
    
  print()
  
  # root = delete(root, 30) #* 노드 30 삭제
  # display(root, "[Delete 30] : ")
  
  # root = delete(root, 26) #* 노드 26 삭제
  # display(root, "[Delete 26] : ")
  
  # root = delete(root, 18) #* 노드 18 삭제
  # display(root, "[Delete 18] : ")
  
  root = delete(root, 35)
  display(root, "[Delete 35] : ")