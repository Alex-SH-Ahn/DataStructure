class ArraySet:
    def __init__(self, capacity = 100):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.capacity
    
    def display(self):
        for i in range(self.size):
            print(self.array[i], end=' ')
        print()
    
    def contains(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                return True
        return False
    
    def insert(self, e):
        if not self.contains(e) and not self.isFull():
            self.array[self.size] = e
            self.size += 1
        else: pass
    
    def delete(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                self.array[i] = self.array[self.size-1]
                #삭제할 자리에 가장 뒤에 있는 요소를 그냥 덮어씌우기!
                self.size -= 1
                return

    def union(self, setB):
        setC = ArraySet()
        for i in range(self.size):
            setC.insert(self.array[i]) 
        for i in range(setB.size):
            setC.insert(setB.array[i]) #겹치는거 빼고 들어가게 됨
        return setC
    
    def intersection(self, setB):
        setC = ArraySet()
        for i in range(self.size):
            if setB.contains(self.array[i]):
                setC.insert(self.array[i])
        return setC
    
    def difference(self, setB):
        setC = ArraySet()
        for i in range(self.size):
            if not setB.contains(self.array[i]):
                setC.insert(self.array[i])
        return setC

    def __add__(self, setB):
        setC = ArraySet()
        for i in range(self.size):
            setC.insert(self.array[i])
        for i in range(self.size):
            setC.insert(setB.array[i])
        return setC
    
    def __and__(self, setB):
        setC = ArraySet()
        for i in range(self.size):
            if setB.contains(self.array[i]):
                setC.insert(self.array[i])
        return setC

    def __sub__(self, setB):
        setC = ArraySet()
        for i in range(self.size):
            if not setB.contains(self.array[i]):
                setC.insert(self.array[i])
        return setC

if __name__ == '__main__':
    S = ArraySet()
    S.insert(10)
    S.insert(20)
    S.insert(30)
    S.insert(40)
    S.display()

    T = ArraySet()
    T.insert(40)
    T.insert(50)
    T.insert(60)
    T.insert(70)
    T.display()

    print('union: ', end='')
    S.union(T).display()
    print('intersection: ', end='')
    S.intersection(T).display()
    print('difference: ', end='')
    S.difference(T).display()

    print('연산자 중복기법으로 만들기')

    intersection_set = S & T
    intersection_set.display()

    difference_set = S - T
    difference_set.display()

    #해야할 것
    #교집합, 차집합 연산
    #print(S==T) : 연산자 중복기법으로 만들기