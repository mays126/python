attempts = 10
while True:
    print("Висят " + str(attempts) + " " + "зелёных бутылок на стене и если одна случайно упадёт")
    a = int(input("Сколько зелёных бутылок на висит на стене?: "))
    attempts -= 1
    if attempts == 0:
        print("Зелёных бутылок не осталось")
        break
    elif a == attempts:
        print(str(attempts)+ " " + "висят на стене")
    else:
        print("Нет попробуй ещё раз")
        continue    

