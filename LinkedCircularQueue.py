class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
    
class LinkedCircularQueue(Node):
    def __init__(self):
        self.tail = None
        self.size = 0
        
    def isEmpty(self):
        return self.tail == None

    def enqueue(self, data):
        node = Node(data, None) #* node라는 이름의 변수가 첫 노드를 가리킴
        if self.isEmpty(): #* self = circular queue
            node.next = node #* 비어있다면 node = 처음이자 마지막 노드 -> node.next = node
            self.tail = node #* tail이 node 자신을 가리키도록
            #! tail = next = node = 첫번째이자 마지막 노드
        else: #* insertLast
            node.next = self.tail.next #* 현재 첫번째 노드가 next가 됨
            self.tail.next = node
            self.tail = node #* 마지막 노드를 가리키도록
        self.size += 1
    
    def dequeue(self): #* deleteFirst
        if not self.isEmpty():
            # #? 내가 작성한 코드
            # data = self.tail.next.data
            # if self.tail == self.tail.next: # 마지막 노드가 자기 자신을 가리키면 -> 1개의 노드만 존재
            #     self.tail = None
            # else:
            #     self.tail.next = self.tail.next.next # 마지막 노드의 다음 노드 = 첫번째 노드 -> 첫번째 노드를 무시하고 그 다음 노드를 가리키도록 함
            # self.size -= 1
            # return data
            #! 정답 코드
            p = self.tail #* 마지막 노드
            q = p.next #* 첫번째 노드(삭제될 노드)
            data = q.data
            if p == q: #* 마지막 노드와 첫번째 노드가 같다면 -> 1개의 노드만 존재 (체크하지 않으면 선형큐에서 문제가 됨)
                self.tail = None #* 초기화
            else:
                p.next = q.next
            self.size -= 1
            return data
            
        else:
            print("Queue is empty")
    
    def display(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        else:
            p = self.tail.next #* 첫번째 노드
            for i in range(self.size):
                print('[%s] -> ' % p.data, end = '')
                p = p.next
            print('\b\b\b   ')

if __name__ == "__main__":
    Q = LinkedCircularQueue()
    
    Q.enqueue('A'); Q.display()
    Q.enqueue('C'); Q.display()
    Q.enqueue('B'); Q.display()
    
    print("Is Linked queue empty? ", Q.isEmpty())
    print("Size of the Linked queue: ", Q.size)
    
    print('[%s] is deleted' % Q.dequeue()); Q.display()