import random

class Hero:
    def __init__(self):
        self.__power = 25
        print("Перс на месте")

    def buff(self,value):
        self.__power += value

    def power(self):
        return self.__power
class Artefact:
    def __init__(self):
        self.__power = random.randint(10,80)
        print("Артефакт на месте")

    def power(self):
        return __power
class Monster:
    def __init__(self):
        self.__power = random.randint(5,100)
        print("Монстр на месте")
    def power(self):
        return self.__power
hero = Hero()
artefact = Artefact()
monster = Monster()
levels = [random.randint(0,1) for i in range(10)]
attempts = []
while True:
    a = int(input("Введите номер двери в которую хотите зайти (от 0 до 9): "))
    attempts.append(random.randint(0,10))
    
    if levels[a] == 0:
        b = random.randint(10,80)
        hero.buff(b)
        print("Герой был усилен на " + str(b) + " очков")
    else:
        c = random.randint(5,100)
        print("За дверью оказался монстр с силой в " + str(c) + " очков")
        if hero.power() >= c:
            print("В этой схватке ты победил!")
        else:
            print("Ты проиграл в неравном бою!")
            exit()
    if len(attempts) >= 10:
        print("Ты победил в этой схватке!")
        break



      
