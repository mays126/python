menu = []

with open('cars.txt', 'r') as file:
    for line in file:
        buf = line.split(' ')
        menu.append({
            'id': int(buf[0]),
            'title': buf[1],
            'id parrent': int(buf[2][0])
            })

for item in menu:
    print(item)
print('\n')

for i in range(len(menu)):
    if menu[i]['id parrent'] == 0:
        print(menu[i]['title'])
        for item in menu:
            if item['id parrent'] == menu[i]['id']:
                print('\t', item['title'])
                for elem in menu:
                    if elem['id parrent'] == item['id']:
                        print('\t\t', elem['title'])