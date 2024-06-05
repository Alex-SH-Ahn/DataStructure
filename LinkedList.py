class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedStack:
    def __init__(self):
        self.top = None
    
    def isEmpty(self): return self.top == None
    def clear(self): self.top = None

    def push(self, item):
        n = Node(item, self.top)
        self.top = n
    
    def pop(self):
        if not self.isEmpty():
            n = self.top
            self.top = n.link
            return n.data
    
    def peek(self):
        if not self.isEmpty():
            return self.top.data
    
    def size(self):
        n = self.top
        count = 0
        while n != None:
            count += 1
            n = n.link
        return count
    
    def display(self, msg):
        print(msg, end='')
        n = self.top
        while n != None:
            print(n.data, end=' ')
            n = n.link
        print()
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self): return self.size == 0
    def clear(self): self.head = None
    def size(self):
        n = self.head
        count = 0
        while n != None:
            count += 1
            n = n.link
        return count

    def display(self, msg):
        print(msg, end='')
        n = self.head
        while n != None:
            print(n.data, end=' ')
            n = n.link
        print()
    
    def getNode(self, pos):
        if pos < 0: return None
        node = self.head
        while pos > 0 and node != None:
            node = node.link
            pos -= 1
        return node
    
    def getEntry(self, pos):
        node = self.getNode(pos)
        if node == None: return None
        else: return node.data
    
    def insert(self, pos, data):
        before = self.getNode(pos)

        if before == None: # 앞에 아무것도 없다면(pos이 1인 경우) 가장 앞에 놓기
            self.head = Node(data, self.head)
        else:
            node = Node(data, before.next)
            before.next = node
        self.size += 1
    # def delete(self, pos):
    #     before = self.getNode(pos-1)
    #     if before == None:
    #         if self.head == None: return None
    #         self.head = self.head.link
    #     else:
    #         if before.link == None: return None
    #         before.link = before.link.link
    
    def insertFirst(self, elem):
        self.head = Node(elem, self.head)
        self.size += 1
    
    #! 정답
    def delete(self, pos): # pos를 삭제, pos - 1의 링크를 pos + 1로 연결
        if self.isEmpty(): print('No element to delete'); return
        
        if pos == 1:
            return self.deleteFirst() #주의할 점: 리턴 필수! main함수 쪽으로 다시 값을 보내주기
        else:
            if (pos <= self.size):
                q = self.getNode(pos) # getnode는 pos 이전 노드의 주소(위치)
                p = self.getNode(pos + 1) # 다음 노드의 위치 받아오기
                
                q.next = p.next
                self.size -= 1
                return p.data
            else:
                print("Invalid position")

    def deleteFirst(self):
        # if self.head == None: return None
        # else:
        #     self.head = self.head.link

        #! 정답: head 포인터가 가리키는 변수를 삭제하고, head 포인터가 다음 노드를 가리키도록
        if self.isEmpty(): print("No element to delete")
        else: 
            p = self.head
            self.head = p.next # 다음 노드를 가리키도록함
            self.size -= 1 # 사이즈 줄이기
            return p.data
    
    def display(self):
        p = self.head
        while p != None:
            print('[%s] -> ' % p.data, end='')
            p = p.next
        print('\b\b\b   ')

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            current = self.head
            while current.link is not None:
                current = current.link
            current.link = Node(data)

if __name__ == "__main__":
    L = LinkedList()
    L.insertFirst('A'); L.insertFirst('B'); L.display()
    L.insert(2, 'C'); L.insert(1, 'D'); L.display()
    L.insert(4, 'E'); L.insert(5, 'F'); L.display(); print()
    
    print('[%s] is deleted', L.delete(2)); L.display()

class LinkedQueue:
    def __init__(self):
        self.tail = None
    
    def isEmpty(self): return self.tail == None
    def clear(self): return False #* 연결된 구조에서 포화상태는 의미X

    def enqueue(self, item):
        node = Node(item, None)
        if self.isEmpty():
            self.tail = node
            node.link = node
        else:
            node.link = self.tail.link
            self.tail.link = node
            self.tail = node
    
    def dequeue(self):
        if not self.isEmpty():
            data = self.tail.link.data #*반환할 데이타
            if self.tail.link == self.tail:
                self.tail = None
            else:
                self.tail.link = self.tail.link.link
            return data
