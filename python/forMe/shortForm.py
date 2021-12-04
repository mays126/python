formulas = ["(a + b)^2","(a-b)^2","a^2-b^2"]
a = int(input("Введите номер формулы из представленных " + str(formulas)))
if a == 0:
    b = int(input("Число первое: "))
    c = int(input("Число второе: "))
    res1 = b**2 + c**2 + 2*b*c
    print(res1)
elif a == 1:
    b = int(input("Число первое: "))
    c = int(input("Число второе: "))
    res1 = b**2 + c**2 - 2*b*c
    print(res1)
else:
    b = int(input("Число первое: "))
    c = int(input("Число второе: "))
    res1 = b**2 - c**2
    print(res1)
