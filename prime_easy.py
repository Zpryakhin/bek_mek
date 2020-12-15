import math
def Is_Prime(a):
    ans = True
    b = round(math.sqrt(a))
    i = 2
    while i <= b:
        if a % (i) == 0:
            ans = False
            break
        i += 1
    return ans    
a = int(input("Введите число: "))    
#if Is_Prime(a):
#    print("Число ", a, " простое")
#else:
#    print("Число ", a, " составное")
print(Is_Prime(a))        