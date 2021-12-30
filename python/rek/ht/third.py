def nums(n):
    if n > 0:
        return n % 10 + nums(n // 10)
    else:
        return 0
print(nums(int(input(">>> "))))        
