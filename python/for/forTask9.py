counter = input("В какую сторону вести отсчёт? r/s: ")
i = 20
if counter == "s":
    num1 = int(input("Введите число: "))
    for r in range(1,num1+1):
        print(r)
elif counter == "r":
    num2 = int(input("Введите число до 20: "))
    while i > num2-1:
        print(i)
        i -= 1
else:
    print("Введено не правильно значение отсчёта!")    
    
    

