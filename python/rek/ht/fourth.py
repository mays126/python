def nums(n):
    if n > 0:
        print(n % 10)
        nums(n // 10)        
nums(int(input('>>> ')))        