str1 = 'Hello'
str2 = "Hi"

str_concat = 'String Concat : ' + str1 + ', ' + str2

print(str_concat)
print(f'str1[0] : {str1[0]}')

hobby = 'swimming'
age = 23
score = 3.75

print("Hobby is %s. Age : %d, Score : %.2f" % (hobby, age, score))

L1 = [3, 5, 7, 9]
L2 = ['A', 'B', 'C', 'D']

print(L1)
print('L1[1] =', L1[1])

L2[2] = 'F'
print('L2:', L2)

L1.append(11)
print('L1:', L1)

print(L1.pop())
print('L1:', L1)

print(L2.count('B'))
L1.insert(2, 100)
print(L1)

map = {'apple' : '사과', 'banana' : '바나나', 'pear' : '배'}
print(map)

for e in map:
  print('key: ', e, end=' / ')
  print('value: ', map[e])

map['grape'] = '포도'
print(map)

map.update({'orange':'오렌지', 'strawberry':'딸기'}) #여러개의 키밸류값 추가
print(map)

print(map.keys()) #꼭 기억해야하는 딕셔너리 함수 두개!
print(map.values())
  