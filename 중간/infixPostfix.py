from ArrayStack import ArrayStack

def precedence(op): # 연산자 우선순위를 정해주는 함수
    if (op == '(' or op == ')'): return 0
    elif (op == '+' or op == '-'): return 1
    elif (op == '*' or op == '/'): return 2
    else: 
        return -1

def infixPostfix(expr):
    S = ArrayStack(100)
    postfix = []

    for term in expr: # 수식의 항이 들어옴
        if term in '(':
            S.push('(')
        elif term in ')':
            while not S.isEmpty():
                op = S.pop()
                if op == '(':
                    break
                else:
                    postfix.append(op)
        elif term in '+-*/':
            while not S.isEmpty():
                op = S.peek()
                if (precedence(term) <= precedence(op)):
                    postfix.append(op)
                    S.pop()
                else: break
            S.push(term)
        else:
            postfix.append(term) #피연산자일 경우
    
    while not S.isEmpty():
        postfix.append(S.pop())
    
    return postfix

if __name__ == '__main__':
    infix = input('Input Infix Expression: ') # 중위표기식 입력받기
    expr = infix.split()
    postfix = infixPostfix(expr)

    print(postfix)