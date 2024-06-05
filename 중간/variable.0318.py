pi = 3.141592
perimeter = 0

def calc_perimeter(radius):
    global perimeter
    print(f'PI = {pi}')
    perimeter = 2 * pi * radius
    print(f'circumference = {perimeter}')

if __name__ == '__main__':
    calc_perimeter(10)
    print(f'globale perimeter = {perimeter}')