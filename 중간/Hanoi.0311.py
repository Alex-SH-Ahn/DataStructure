def hanoiTower(n, fr, tmp, to):
    if (n==1):
        print(f'Disk {n} : {fr} ---> {to}')
    else:
        #1. n-1개의 원판을 from에서 temp로 이동
        hanoiTower(n-1, fr, to, tmp) #n-1이 가운데로 이동
        print(f'Disk {n} : {fr} ---> {to}')
        #2. 가운데 원판을 tmp에서 to로 옮기기
        hanoiTower(n-1, tmp, fr, to)

hanoiTower(4, 'A', 'B', 'C') #기둥 이름이 A, B, C로 정의
