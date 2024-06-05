from CircularQueue import *

class CircularDeque(CircularQueue): # CircularQueue 상속받기
    def __init__(self, capacity=10):
        super().__init__(capacity)
    
    def display(self):
        i = self.front
        while (i + 1) % self.capacity != self.rear:
            i = (i + 1) % self.capacity
            print('[%c]' % self.queue[i], end=' ')
        print()

        # while i != self.rear:
        #     i = (i + 1) % self.capacity
        #     print('[%c]' % (self.queue[i]), end=' ')
        # print()

    def addRear(self, e):
        self.enqueue(e)
    
    def deleteFront(self):
        self.dequeue()
    
    def getFront(self):
        self.peek()
    
    def addFront(self, e):
        # 내가 해본 것:
        # if not self.isFull():
        #     self.front = (self.front - 1 + self.capacity) % self.capacity #front 반시계이동
        #     self.queue[self.front] = e
        # else:
        #     print('Overflow')

        if not self.isFull():
            self.queue[self.front] = e #self.front는 비어있으므로 그냥 거기에 넣으면 됨!
            self.front = (self.front - 1 + self.capacity) % self.capacity
        else:
            print('Overflow')


    def deleteRear(self):
        # 내가 해본 것:
        # if not self.isEmpty():
        #     self.rear = (self.rear - 1 + self.capacity) % self.capacity #rear 반시계이동
        #     return self.queue[self.rear]
        # else:
        #     print('Underflow')

        if not self.isEmpty():
            e = self.queue[self.rear] #리턴을 해줘야하기 때문에
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
            return e
        else:
            print('Underflow')

    def getRear(self):
        # 내가 해본 것:
        # if not self.isEmpty():
        #     return self.queue[(self.rear) % self.capacity] #여긴 잘 모르겟음 ㅜ
        # else:
        #     print('Underflow')

        if not self.isEmpty():
            return self.queue[self.rear]
        else:
            print('Underflow')

# 테스트 코드
if __name__ == "__main__":
    import random
    DQ = CircularDeque()

    for i in range(4):
        DQ.addFront(random.randint(65, 90))
    DQ.display()

    for i in range(4):
        DQ.addRear(random.randint(65, 90))
    DQ.display()
    
    for i in range(2):
        DQ.deleteFront()
    DQ.display()
    
    for i in range(2):
        DQ.deleteRear()
    DQ.display()