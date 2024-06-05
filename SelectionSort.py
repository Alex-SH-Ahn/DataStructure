def printStep(A, index):
  print('               Step %d : ' % index, end='')
  print(A)

def selectionSort(A):
  n = len(A)
  
  for i in range(n-1):
    least = i
    for j in range(i+1, n):
      if A[j] < A[least]:
        least = j
    A[i], A[least] = A[least], A[i]
    #* printStep(A, i+1) #* i는 0부터 시작하므로 1을 더해줌

def insertionSort(A):
  n = len(A)
  
  for i in range(1, n):
    key = A[i] #* 내 오른손에 든 카드
    j = i - 1 #* i의 한 칸 왼쪽부터 시작
    while j >= 0 and A[j] > key: #* 모든 카드가 1장보다 많고, 내 왼손에 든 카드가 오른손에 든 카드보다 클때
      A[j+1] = A[j] #* 
      j -= 1
    A[j+1] = key
    printStep(A, i) #* i는 1부터 시작하므로 그냥 i

if __name__ == "__main__":
  data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
  
  L = list(data)
  
  print("Before Selection Sort :", L)
  selectionSort(L)
  print(" After Selection Sort :", L)
  
  print()
  print("----------------------------------------------------")
  print()
  
  data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
  
  L = list(data)
  
  print("Before Insertion Sort :", L)
  insertionSort(L)
  print(" After Insertion Sort :", L)