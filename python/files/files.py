from collections import Counter
f = open('pwd.txt', 'r' )
arr = []

for i in f:
    a = i.split(';')
    a.reverse()
    arr.append(a[0])
arr.remove(arr[0])      
print(arr)
c = Counter(arr)
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')

print("Наиболее частые 10 паролей: " + str(c.most_common(10)))

