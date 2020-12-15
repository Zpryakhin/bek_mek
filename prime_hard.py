import math
def Is_Prime(a):
    ans = False
    b = math.factorial(a-1)
    #По теореме Вильсона, если p простое, то (p-1)! = -1 mod p или (p-1)! + 1 = 0 mod p
    if (b + 1) % a == 0:
        ans = True
    return ans
a = int(input("Введите число: "))
#if Is_Prime(a):
#    print("Простое")
#else:
#    print("Составное") 
print(Is_Prime(a))   

