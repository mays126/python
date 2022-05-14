from random import randint 

num = randint(1,10)
color = randint(1,2)
attempts = 0

while attempts < 5:
    attempt = input('Введите номер и цвет: ')
    if color == 1:
        col = 'красный'
    else:
        col = 'чёрный'    
    if int(attempt[0]) == num and attempt[2::] == col:
        print('Верно!')
        break
    attempts += 1
else:
    print('Правильный ответ:',attempt[0],col)