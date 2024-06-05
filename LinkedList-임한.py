
class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class ListType:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.head == None
    
    def getNode(self, pos):
        p = self.head
        if pos == 1:  # 비어있는 리스트일 경우의 처리는 이미 했다고 가정
            return None # 가장 앞에 있는 index, pos == 1을 선택했기 때문에 그 앞에는 아무것도 없다는 의미에서 None.
        else: # pos이 1이 아닌 경우는 내가 들어갈 곳 앞에 있는 Node를 찾기
            while pos > 2: 
                p = p.next
                pos -= 1
            return p

    def insert(self, pos, data):
        before = self.getNode(pos)

        if before == None: # 앞에 아무것도 없다면(pos이 1인 경우) 가장 앞에 놓기
            self.head = Node(data, self.head)
        else:
            node = Node(data, before.next)
            before.next = node
        self.size += 1

    def delete(self, pos):
        before = self.getNode(pos)

        if before == None:
            if not self.isEmpty():
                self.head = self.head.next
        else:
            before.next = before.next.next
        self.size -= 1

    def display(self):
        p = self.head

        while p != None:
            print('[%s]' % p.data, end="")
            p = p.next
        print()

if __name__ == "__main__":
    L = ListType()

    L.insert(1, 'A')
    L.insert(1, 'B')
    L.insert(3, 'C')
    L.display()

    L.delete(2)
    L.display()


