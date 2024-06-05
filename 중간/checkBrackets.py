from ArrayStack import ArrayStack

def checkBrackets(str):
    S = ArrayStack(100)

    for c in str:
        if c in '[{(<':
            S.push(c)
        elif c in ']})>':
            if S.isEmpty():
                return False
            else:
                left = S.pop()
                if (c == ']' and left != '[') or \
                    (c == '}' and left !='{') or \
                    (c == ')' and left != '(') or \
                    (c == '<' and left != '>'):
                    return False
    
    return S.isEmpty()
    
if __name__ == '__main__':
    s1 = '{ A[(i + 1)] = 0}' #맞음
    s2 = 'if((i == 0) && (j == 0)' #괄호 개수가 안 맞음
    s3 = 'A[(i + 1]) = 0'

    print(s1, '-->', checkBrackets(s1)) #True
    print(s2, '-->', checkBrackets(s2)) #False
    print(s3, '-->', checkBrackets(s3)) #False

    filename = '5.txt'
    inFile = open(filename, 'r')
    str = inFile.read()
    inFile.close()

    print(filename, '-->', checkBrackets(str))