def nums(n):
    if n > 0:
        pritn(n % 10)
        nums(n // 10)        
nums(int(input('>>> ')))        