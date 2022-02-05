def power(base,exp):
    if exp == 0:
        return 1
    return base * power(base,exp - 1)

a = int(input('base: '))
b = int(input('exp: '))
print(power(a,b))