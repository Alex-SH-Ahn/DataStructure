
class ArrayStack:
    def __init__(self, capacity = 100):
        self.capacity = capacity
        self.stack = [None] * self.capacity
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.capacity - 1
    
    def push(self, e):
        if not self.isFull():
            self.top += 1
            self.stack[self.top] = e
        else:
            print('Stack Overflow')
    
    def pop(self):
        if not self.isEmpty(): #요소 함수가 있어야 pop할 수 있음
            e = self.stack[self.top] #맨 위에 있는 애를 빼는 것
            self.top -= 1
            return e
        else:
            print('Empty')
    
    def peek(self):
        if not self.isEmpty():
            return self.stack[self.top]
        else:
            print('Empty')
    
    def sortedPush(self, e): #스택에 넣으면서 정렬하는 것 -> 재귀호출 이용
        if (self.isEmpty() or e > self.peek()): 
            #정렬하려고하는데, 내가 넣기로 하는게 맨 위 요소보다 크면 걍 넣고
            self.push(e)
        else:
            temp = self.pop()
            self.sortedPush(e) #재귀호출
            self.push(temp)

    def display(self):
        #스택 구조에서 보통 display라는 함수가 맞지 않음
        #외부와 연결되어있는 것은 맨 위의 요소 뿐
        #사용자가 접근하지 못하도록 해야함
        print(self.stack[0 : self.top + 1])

if __name__ == '__main__':
    S = ArrayStack(10)
    data = [5, 3, 8, 1, 2, 7]

    for d in data:
        S.sortedPush(d) #정렬되면서 들어가게 됨
        S.display()
    
    print(S.pop()) #pop은 보여주고 삭제
    S.display()

    print(S.peek()) #peek은 보여주기만함
    S.display()

# sortedPush설명은 굿노트 pdf에