

def sum_num(n):
    if n > 0:
        return n % 10 + sum_num(n // 10)
    else:
        return 0


def nums(k,s):
    d = 0
    c = k - 1
    for i in range(10**c, 10**k):
        if sum_num(i) == s:
            d += 1
    return d        

a = int(input('>>>'))
b = int(input('>>>'))
print(nums(a,b))
