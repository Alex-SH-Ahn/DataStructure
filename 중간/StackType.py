from LinkedList import Node, LinkedList
#! 중간고사 3번 문제

S = LinkedList()

def push(data):
    S.insertFirst(data)

def pop():
    return S.deleteFirst()

push('A'); S.display()
push('B' ); S.display()
push('C'); S.display()

print('[%s] is popped' % pop()); S.display()