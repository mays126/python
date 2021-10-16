total = 0
for i in range(0,5):
    num1 = int(input("Введите число: "))
    ask1 = input("Хотите включить данное число в суммирование? y/n: ")
    if ask1 == "y":
        total += num1
print(total)