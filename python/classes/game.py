import random

class Charecter:
    def __init__(self):
        print("Перс на месте.")

    def power(self,value):
        self.value = 25
        return value
class Doors:
    def __init__(self):
        self.doors = [] 
        print("Двери в ад созданы.") 

    def generator(self, value):
        if value == 1:
            self.doors.append("Бафф")
        elif value == 2:
            self.doors.append("Монстр")

    def MaksLen(self):
        if len(self.doors) == 10:
            return "List is full!"

obj = Charecter()
obj2 = Doors()
ChareckPower = 25
t = 0
for i in range(10):
    e = random.randint(1,2)
    obj2.generator(e)
    print(obj2.doors)   
    if print(obj2.MaksLen()) == "List if full!":
        break
kolVoDoors = [0,1,2,3,4,5,6,7,8,9]
while len(kolVoDoors) != 0:
    a = int(input("Введите номер двери из представленных: " + str(kolVoDoors)))
    for i in range(len(kolVoDoors)-1):
        if a == kolVoDoors[i]:
            kolVoDoors.remove(i)
            while t != 1:
                if obj2.doors[a] == "Бафф":
                    b = random.randint(10,80)
                    ChareckPower += b
                    obj.power(ChareckPower)
                    print(ChareckPower)
                elif obj2.doors[a] == "Монстр":
                    c = random.randint(5,100)
                    if ChareckPower < c:
                        ChareckPower -= c
                        print(ChareckPower)          
                    if ChareckPower != 0:                       
                        break
                    else:
                        d = "GAME OVER"
                        break                      
                else:
                    break                   
                t += 1
                

                







