name = input("Введите имя: ")
num = int(input("Введите число: "))
if num <= 10:
    for i in range(num):
        print(name)
elif num <= 0:
    print("To low")
else:
    for i in range(3):
        print("To high")
