
counter = 1
while True:
    name = input("Enter name: ")
    print(name + " " + "has been invited")
    a = input("Хотите позвать кого-то ещё? y/n: ")
    if a == "y":
        counter += 1
        continue
    elif a == "n":
        break
print("Кол-во приглашённых человек: " + str(counter))        
        
