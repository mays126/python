def nums(n):
    if n == 2:
        print('Yes')
    elif n < 2:
        print('No')    
    else:
        nums(n/2)
num = int(input(">>> "))
nums(num)      
