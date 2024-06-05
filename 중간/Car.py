class Car:
    def __init__(self, color, speed=0):
        self.color = color
        self.speed = speed
        if (self.speed > 0):
            self.driving = True
        else: self.driving = False

    def speedUp(self):
        self.speed += 10
        self.driving = True
    
    def speedDown(self):
        self.speed -= 10
        if (self.speed != 0):
            self.driving = True
        else: self.driving = False
    
    def stop(self):
        self.speed == 0
        self.driving = False

    #여기서 self는 나 자신을 호출하는 것. (나랑 비교해야하니까)
    def __eq__(self, other):
        # return self.color == other.color
        return "YES" if self.color == other.color else "NO" #파이썬의 삼항연산자

    def __ge__(self, other):
        return "YES" if self.speed >= other.speed else "NO"

    def __str__(self):
        return f'color: {self.color}, speed: {self.color}, isDriving: {self.driving}'

if __name__ == '__main__':
    myCar = Car('red')
    otherCar = Car('black', 120)
    anotherCar = Car('yellow', 150)
    print(f'myCar: {myCar}\notherCar: {otherCar}\nanotherCar: {anotherCar}')
    print()

    myCar.speedUp()
    otherCar.speedDown()
    print(f'myCar: {myCar}\notherCar: {otherCar}\nanotherCar: {anotherCar}')

    # print(myCar.__eq__(otherCar))
    print(myCar == otherCar)
    print(myCar >= otherCar)
    print(otherCar >= myCar)











