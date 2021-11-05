upperLimit = int(input("Введите до кого числа найти совершенные числа: "))
for n in range(2,upperLimit+1):
    sum = 0
    for d in range(1,n):
        if not n % d:
            sum += d
        if sum == n:           
            print(s, "Совершенное")
                          

