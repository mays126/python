def numsPrint(n):
    if n == 1:
        print(n, end=' ')
    else:
        print(n, end=' ')
        numsPrint(n - 1)
        print(n, end=' ')

numsPrint(5)