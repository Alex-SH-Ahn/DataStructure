#함수 find_min_max
def find_min_max(A): 
    min = A[0]
    max = A[0]

    for i in range (1, len(A)):
        if max < A[i]: max = A[i]
        if min > A[i]: min = A[i]

    return (min, max)

if __name__ == '__main__':
    data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
    (x, y) = find_min_max(data)
    print(f'(min, max)는 {x, y}')

#외부에서 def find_min_max를 실행하면 print까지 실행이 됨.
#이것을 방지하기 위해서는 if __name__ == '__main__': 코드를 추가해야함.
#파일 자체를 실행해야지 if __name__ == '__main__' 밑의 코드가 실행됨
#외부에서 실행하면 이 코드 밑의 실행문들은 작동되지 않음

#함수 sum
def sum_range(begin, end, step=1):
    sum = 0
    for n in range(begin, end, step):
        sum += n
    return sum

if __name__ == "__main__": #
    print(f'sum = {sum_range(1, 10)}')
    print(f'sum = {sum_range(1, 10, 2)}')

    #키워드 인수
    print(f'sum = {sum_range(step=3, begin=1, end=10)}')
    print(f'game ', end=" ")



