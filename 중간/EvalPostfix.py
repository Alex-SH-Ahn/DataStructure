from ArrayStack import ArrayStack

def evalPostfix(expr): # 수식이 들어감 = expression
    S = ArrayStack(100)

    #수식을 여러개의 토큰으로 바꾸기 -> 토큰나이징
    for token in expr:
        if token in '+-*/':
            val2 = S.pop()
            val1 = S.pop()
            if token == '+': S.push(val1 + val2)
            elif token == '-': S.push(val1 - val2)
            elif token == '*': S.push(val1 * val2)
            elif token == '/': S.push(val1 / val2)
        else:
            S.push(float(token))
        
    return S.pop()

if __name__ == '__main__':
    str = '8 2 / 3 - 3 2 * +'
    expr = str.split()

    print('[', str, ']', '-->', evalPostfix(expr))

#후위연산자로 바꿔줘야함
