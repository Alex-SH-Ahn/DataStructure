capacity = 100
array = [None] * 100
size = 0

def isEmpty():
    return size == 0 #True or False 

def isFull():
    return size == capacity #True or False

def insert(pos, e):
    global size
    if not isFull() and (0 <= pos <= size):
        for i in range(size, pos, -1):
            array[i] = array[i-1]
        array[pos] = e
        size += 1
    else: #isFull or invalid position
        print('Overflow or Invlaid Position')

def delete(pos):
    global size
    if not isEmpty() and (0 <= pos < size):
        e = array[pos] #별도의 변수에 저장해두기
        for i in range(pos, size-1):
            array[i] = array[i+1]
        size -= 1
        return e
    else: 
        print('Overflow or Invlaid Position')

def findItem(e):
    for i in range(size):
        if array[i] == e:
            return i
    return -1

def display():
    for i in range(size):
        print(array[i], end=' ')
    print()

if __name__ == '__main__':
    insert(0, 'A')
    insert(1, 'B')
    insert(1, 'C')
    display()

    insert(4, 'D') #size는 3인데, 4번에 넣으려고 해서 overflow
    insert(3, 'E')
    display()

    e = input('Input item to delete : ')
    idx = findItem(e)
    if idx != 1:
        delete(idx)
        display()




