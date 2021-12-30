def nums(a,b):
    if a < b:
        if a + 1 == b: 
            print(a,b)
        else:
            print(a)
            nums(a+1,b)
    else:
        if a - 1 == b:
            print(a,b)
        else:
            print(a)
            nums(a-1,b)  
num1 = int(input(">>> "))    
num2 = int(input(">>> "))
nums(num1,num2)                      
