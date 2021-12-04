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

    def power(self):
        return self.__power
class Monster:
    def __init__(self):
        self.__power = random.randint(5,100)       
    def power(self):
        return self.__power
hero = Hero()
levels = [random.randint(0,1) for i in range(10)]
attempts = []
while True:
    a = int(input("Введите номер двери в которую хотите зайти (от 0 до 9): "))
    attempts.append(random.randint(0,10))
    
    if levels[a] == 0:
        artefact = Artefact()
        hero.buff(artefact.power())
        print("Герой был усилен на " + str(artefact.power()) + " очков")
    else:
        monster = Monster()
        print("За дверью оказался монстр с силой в " + str(monster.power()) + " очков")
        if hero.power() >= monster.power():
            print("В этой схватке ты победил!")
        else:
            print("Ты проиграл в неравном бою!")
            exit()
    if len(attempts) >= 10:
        print("Ты победил в этой битве!")
        break



      
