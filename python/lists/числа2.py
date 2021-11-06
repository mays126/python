nums = []
i = 0
while True:
    i += 1
    a = int(input("Введите число: "))
    nums.append(a)
    print(nums)
    if i % 3 == 0:
        f = input("Хотите удалить последний элемент из списка? y/n: ")
        if f == "y":
            nums.remove(a)
            print(nums)
        else:
            continue


    