def sum_nums(n):
    if n > 0:
        return n % 10 + sum_nums(n // 10)
    else:
        return 0
   


def num(n, nech=0):
    if n == 0:
        print("Нечётных: ",nech)
    else:
        new_n = n % 10
        n = n // 10
        if new_n % 2 != 0:
            nech += 1
        return num(n,nech)


        
g = int(input('>>> '))
print(sum_nums(g))
num(g)
