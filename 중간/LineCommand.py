from ArrayListCl import ArrayList

list = ArrayList()

while True:
    command = input('[메뉴선택] i-입력 d-삭제 r-변경 p-출력 l-읽기 s-저장 q-종료 : ')

    if command == 'i':
        pos = int(input('입력행 번호: '))
        str = input('입력행 내용: ')
        list.insert(pos, str)
    
    elif command == 'd':
        pos = int(input('삭제행 번호: '))
        list.delete(pos)
    
    elif command == 'r':
        pos = int(input('변경행 번호: '))
        str = input('변경행 내용: ')
        list.replace(pos, str) #새로운 함수! replace
    
    elif command == 'p':
        print('Line Editor')
        for line in range(list.size):
            print(f'{[line]}', end=' ')
            print(list.getEntry(line)) #새로운 함수 getEntry
    
    elif command == 'l': #txt파일에 저장
        filename = 'test.txt'
        infile = open(filename, 'r')
        lines = infile.readlines()
        
        for line in lines:
            list.insert(list.size, line.rstrip()) #list에 텍스트 파일을 읽어와서 저장
        
        infile.close()
    
    elif command == 's':
        filename = 'test.txt'
        outfile = open(filename, 'w')
        len = list.size #몇개의 라인이 있는지

        for i in range(len):
            outfile.write(list.getEntry(i) + '\n')
        
        outfile.close()

    elif command == 'q':
        exit()

