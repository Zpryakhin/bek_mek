import math
def Is_Prime(a):
    ans = False
    b = math.factorial(a-1)
    #По теореме Вильсона, если p простое, то (p-1)! = -1 mod p или (p-1)! + 1 = 0 mod p
    if (b + 1) % a == 0:
        ans = True
    return ans

