import random
from SelectionSort import selectionSort

def rBinarySearch(A, key, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
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
  return -1 #* 반복문을 빠져나왔는데도 찾지 못했다면 -1을 반환

if __name__ == '__main__':
  A = []
  for i in range(15):
    A.append(random.randint(1, 100)) #* 난수발생
  selectionSort(A) #* 정렬
  #! selectionSort의 printStep 지움
  print('A[] = ', A)
  
  key = int(input('Input Search Key : '))
  print('rBinarySearch : %d' % rBinarySearch(A, key, 0, 14)) #* 이진탐색