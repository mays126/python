
while True:
    number = int(input("Введите число: "))
    if number < 10:
        print("Too low")
        continue
    elif number > 20:
        print("Too high")
        continue
    else:
        print("Thank you")
        break        
