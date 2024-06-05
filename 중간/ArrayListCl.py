#함수 버전으로 사용한다면 Array를 한 개밖에 사용할 수 없음

class ArrayList:
    def __init__(self): #함수버전에서 만든 전역변수를 멤버변수로 선언
        self.capacity = 100
        self.size = 0
        self.array = [None] * self.capacity
    
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.capacity == self.size
    
    def insert(self, pos, e):
        if not self.isFull() and 0 <= pos <= self.size: # valid position?
            for i in range(self.size, pos, -1):
                self.array[i] = self.array[i-1]
            self.size += 1
            self.array[pos] = e
        else:
            print('Overflow or Invalid Position')
    
    def delete(self, pos):
        if not self.isEmpty() and (0 <= pos < self.size):
            #self.size와 pos가 같으면 존재하지 않는 element
            e = self.array[pos]
            for i in range(pos, self.size-1):
                self.array[i] = self.array[i+1]
            self.size -= 1
            return e
        else:
            print('Overflow or Invalid Position')
    
    def replace(self, pos, e):
        if 0 <= pos < self.size:
            self.array[pos] = e #그 자리의 요소를 덮어쓰기
        else: pass
    
    def getEntry(self, pos):
        if 0 <= pos < self.size:
            return self.array[pos]
        else: return None
    
    def findItem(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                return i
        return -1

    def display(self):
        for i in range(self.size):
            print(self.array[i], end=' ')
        print()

if __name__ == '__main__':
    arr1 = ArrayList()
    arr1.insert(0, 'A')
    arr1.insert(1, 'B')
    arr1.insert(1, 'C')
    arr1.display()

    arr1.insert(4, 'D')
    arr1.insert(3, 'E')
    arr1.display()

    arr1.delete(3)
    arr1.display()

    print(arr1.findItem('A'))

    #test code
    #L1 = ArrayList(50)
    L1 = ArrayList()
    L1.insert(0, 10)
    L1.insert(1, 20)
    L1.insert(1, 30)
    L1.display()
