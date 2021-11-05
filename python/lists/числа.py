nums = [111,222,333,444]
print(nums,sep = "\n")
a = int(input("Введите число: "))
for i in nums:
    if a == i:
        print(nums.index(i))
        break
    else:
        continue    
    print("Этого нет в списке")    