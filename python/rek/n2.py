def num(n):
    if n == 1:
        print(n, end = ' ')
    else:
        print(n, end = ' ')
        num(n-1)
num(5)
