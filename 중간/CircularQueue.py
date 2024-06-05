class CircularQueue:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.queue = [None] * self.capacity
        self.front = 0
        self.rear = 0
    
    def isEmpty(self):
        return self.front == self.rear
    
    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity
    
    def enqueue(self, e):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = e
        else:
            print('Overflow')
    
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.queue[self.front]
        #엘리먼트를 없애는 부분이 없는데요?
        #front가 움직이는 것 자체가 삭제를 의미하고 있음 (어차피 enqueue하면 그 자리에 다른 것으로 덮어쓰게 됨)
        else:
            print('Underflow')
    
    def peek(self):
        if not self.isEmpty():
            return self.queue[(self.front + 1) % self.capacity]
        else:
            print('Underflow')
    
    def display(self): #원형큐에서 가장 어려운 부분
        print(f'Front : {self.front}, Rear: {self.rear}')
        i = self.front
        
        while i != self.rear:
            i = (i + 1) % self.capacity
            print(f'[{self.queue[i]}] ', end='')

if __name__ == "__main__":
    Q = CircularQueue()
    Q.enqueue('A')
    Q.enqueue('B')
    Q.enqueue('C')
    Q.enqueue('D')
    Q.enqueue('E')
    Q.display()
    print()

    print(f'Dequeue --> {Q.dequeue()}')
    print(f'Dequeue --> {Q.dequeue()}')
    print(f'Dequeue --> {Q.dequeue()}')
    Q.display()
    print()

    Q.enqueue('F')
    Q.enqueue('G')
    Q.enqueue('H')
    Q.enqueue('I')
    Q.display()
    print()