count_rFib = 0

def rFib(n):
    global count_rFib #전역변수 
    count_rFib += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rFib(n-2) + rFib(n-1)

print('rFib : %d' % (rFib(10)))
print(f'rFib count : {count_rFib}')

def iFib(n): #메모이제이션: 메모 기반으로 작성 
    #문제: 똑같은 함수를 계속 사용 -> 메모를 작성하는 것처럼 다른 곳에 저장해두는 것.
    if n < 2:
        return n;
    pp = 0 #전전
    p = 1 #전
    for i in range(2, n+1):
        current = p + pp
        pp = p
        p = current
    
    return current

print('iFib : %d' % (iFib(10)))
#최고차항의 차수가 제일 중요하다!