import math
a = int(input("Введите число: "))
ans = False
b = math.factorial(a-1)
#По теореме Вильсона, если p простое, то (p-1)! = -1 mod p или (p-1)! + 1 = 0 mod p
if (b + 1) % a == 0:
    ans = True
if ans:
    print("Число ", a, " простое")
else:
    print("Число ", a, " составное")  