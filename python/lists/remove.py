objects = ["Математика","Английский", "Русский", "Литература","Биология","География"]
print(objects)
a = input("Какие из этих предметов вам больше всего ненравятся: ")
objects.remove(a)
objects.sort()
print(objects)