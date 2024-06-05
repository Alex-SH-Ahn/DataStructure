#상속은 트리의 형태
from Car import Car

class SuperCar(Car):
    def __init__(self, color, speed = 0, bTurbo = True):
        super.__init__(color, speed)
        self.bTurbo = bTurbo

    def setTurbo(self, bTurbo = True):
        self.bTurbo = bTurbo

    def speedUp(self):
        if self.bTurbo: self.speed += 50
        else: super().speedUp()

    def str(self):
        if self.bTurbo:
            return '[%s][speed = %s] Turbo' %(self.color, self.speed)
        else:
            return '[%s][speed] = %s Normal' %(self.color, self.speed)

if __name__ == '__main__':
    s1 = SuperCar("Gold")
    s2 = SuperCar("White", 50, False)

    s1.speedUp(); s2.speedUp()

    print('s1: ', s1)
    print('s2: ', s2)