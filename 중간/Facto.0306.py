def iFact(n): #iterable factorial
    result = 1 # 대입연산
    for i in range(n, 0, -1):
        result = result * i 
        # 대입연산 + 곱하기 연산(n번 반복) => 선형시간복잡도
    return result

print('iFact : %d' % (iFact(5)))

def rFact(n): # recursion Factorial
    # 절대 반복문이 나오면 안됨! 무조건 조건문
    if (n == 1) :
        return 1
    else:
        return n * rFact(n-1) 
        #재귀함수, 순환함수 : 나 자신을 소환

print('rFact : %d' % (rFact(5)))
