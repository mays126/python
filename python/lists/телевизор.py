programs = ["Первый","Спорт","Музыка","Вести"]
for i in range(len(programs)):
    print(programs[i])
a = input("Введите название ещё одной передачи: ")
b = int(input("Введите место в списке на котором оно будет стоять: "))
programs.insert(b,a)
print(programs)