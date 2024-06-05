from EvalPostfix import evalPostfix
from infixPostfix import infixPostfix

infix = input('Input Infix Expression: ') # 중위표기식 입력받기
expr = infix.split()

print('Answer: ', expr, '=', evalPostfix(infixPostfix(expr)))
print('Postfix: ', infixPostfix(expr))