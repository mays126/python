def DifferenceBeetwenStringLengthes(str1,str2):
    str1 = len(str1)
    str2 = len(str2)
    if str1 > str2:
        return str1
    elif str2 > str1:
        return str2
    else:
        return str1,str2

def DifferenceBeetwenStringSymbols(str1,str2):
    if str1 > str2:
        return str1
    elif str2 > str1:
        return str2
    else:
        return str1,str2


print(DifferenceBeetwenStringSymbols('Строка один','Строка два'))
print(DifferenceBeetwenStringLengthes('Строка один','Строка два'))
