a = input("Введите имя приглашённого: ")
b = input("Введите имя приглашённого: ")
c = input("Введите имя приглашённого: ")
names = [a,b,c]
print(names)
while True:
    a = input("Хотите приглосить кого то ещё? y/n: ")
    if a == "y":
        d = input("Введите имя приглашённого: ")
        names.append(d)
    elif a == "n":
        print(len(names))
        break
    else:
        continue        
            