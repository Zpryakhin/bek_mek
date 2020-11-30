import math
a = int(input("Введите число: "))
ans = True
b = round(math.sqrt(a))
i = 2
while i <= b:
    if a % (i) == 0:
        ans = False
        break
    i = i + 1
if ans:
    print("Число ", a, " простое")
else:
    print("Число ", a, " составное")        