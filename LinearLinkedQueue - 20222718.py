class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedLinearQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    
    def isEmpty(self): return (self.rear == None and self.front == None)
    
    def enqueue(self, data):
        node = Node(data, None)
        if self.isEmpty(): #비어있는 큐라면 rear = front
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            #삽입을 했으니 rear를 새로운 노드로 이동
            self.rear = node # rear도 맨 끝으로 이동
        self.size += 1
        
    def dequeue(self):
        if not self.isEmpty(): #큐에 노드가 존재
            data = self.front.data #맨 앞 데이터 저장
            if self.front == self.rear: #큐에 노드가 1개만 존재
                self.front = None
                self.rear = None
                self.size -= 1
                return data
            else:
                self.front = self.front.next #front가 다음 노드로 이동
            self.size -= 1
            return data
        else:
            print("Queue is empty")
    
    def display(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        else:
            p = self.front
            for i in range(self.size):
                print('[%s] -> ' % p.data, end = '')
                p = p.next
            print('\b\b\b   ')

if __name__ == "__main__":
    Q = LinkedLinearQueue()
    
    Q.enqueue('A'); Q.display()
    Q.enqueue('C'); Q.display()
    Q.enqueue('B'); Q.display()
    
    print("Is Linked queue empty? ", Q.isEmpty())
    print("Size of the Linked queue: ", Q.size)
    
    print('[%s] is deleted' % Q.dequeue()); Q.display()