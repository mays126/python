arr = []

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
            arr.append(d)

a = int(input('>>>'))
b = int(input('>>>'))
nums(a,b)

arr.sort(reverse=True)
print(arr[0])