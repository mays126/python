nums = [111,222,333,444]
for i in range(len(nums)):
    print(nums[i])
a = int(input("Введите число: "))
for i in nums:
    if a == i:
        print(nums.index(i))
        break
    else:
        continue    
    print("Этого нет в списке")    