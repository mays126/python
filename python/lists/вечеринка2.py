a = input("Введите имя приглашённого: ")
b = input("Введите имя приглашённого: ")
c = input("Введите имя приглашённого: ")
names = [a,b,c]
print(names)
while True:
    removeName = input("Введите имя человека в списке: ")
    a = input("Хотите что бы этот человек присутвствовал на вечеринке? y/n: ")
    if a == "n":
        names.remove(removeName)
        print(names)
        break
    else:
        break    
