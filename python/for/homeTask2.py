compnum = 50
counter = 1
while True:
    num = int(input("Enter number: "))
    if num < compnum:
        print("Введёное число меньше")
        counter += 1
        continue       
    elif num > compnum:
        print("Введёное число больше")
        counter += 1
        continue
    else:
        print("Well done you took " + str(counter) + " " + "attempts")  
        break  