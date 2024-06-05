class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedStack:
    def __init__(self):
        self.top = None
        self.size = 0
        
    def isEmpty(self): return self.top == None
    def clear(self): self.top = None
    
    def push(self, data):
        node = Node(data, self.top) # 새 노드를 만들고
        self.top = node # 그 노드가 가장 위에 잇으므로 top이 가리키게
        self.size += 1
    
    def pop(self):
        if not self.isEmpty():
            p = self.top
            data = p.data
            self.top = p.next # 그 다음 노드가 top이 됨
            self.size -= 1 # pop을 했으니 사이즈 줄이기
            return data
        else:
            print("Stack is Empty")
            
    def peek(self):
        if not self.isEmpty():
            return self.top.data
        else:
            print("Stack is Empty")
    
    def display(self):
        p = self.top
        while p != None:
            print('[%s] -> ' % p.data, end='')
            p = p.next
        print('\b\b\b   ')
        

if __name__ == "__main__":
    S = LinkedStack();
    
    S.push('A'); S.push('B'); S.push('C')
    S.display()

    print('Pop : [%s]' %S.pop()); S.display()
    print('Peek : [%s]' %S.peek()); S.display()


