class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class StackType:
    def __init__(self):
        self.top = None
        self.size = 0 # 있어도 되고 없어도 됨. 있으면 매우 편함. 하지만 어딘가에서 실수로 빠트리면 에러가 안뜨기 때문에 위험

    def isEmpty(self):
        return self.top == None
    
    def push(self, data): # insertFirst()
        node = Node(data, self.top)  # 내가 누굴 point하고 
        self.top = node # 누가 나를 point하나
        self.size += 1

    def pop(self):
        if not self.isEmpty():
            p = self.top
            data = p.data
            self.top = p.next
            self.size -= 1
            return data
        else: pass

    def peek(self):
        if not self.isEmpty():
            return self.top.data
        else: pass

    def display(self):
        p = self.top
        
        while p != None:
            print('[%s] -> ' %p.data, end='')
            p = p.next
        print('\b\b\b   ')
        

if __name__ == "__main__":
    S = StackType()

    S.push('B'); S.push('A'); S.push('C')
    S.display()

    print('Pop : %s' %S.pop()); S.display()
    print('Peek : %s' %S.peek()); S.display()






