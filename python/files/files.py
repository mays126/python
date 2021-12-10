
f = open('pwd.txt', 'r' )
arr = []
for i in f:
    a = i.split(';')
    a.reverse()
    arr.append(a[0])
arr.remove(arr[0])      
print(arr)
mostCommon = None
insides = 0
for i in arr:
    d = arr.count(i)
    if d > insides:
        insides = d
        mostCommon = i            
          
print("Наиболее популярное: " + mostCommon)

