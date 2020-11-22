a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
#a = 47
#b = 50
def gcdC(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = gcdC(b, a % b)
        return d, y, x - y * (a // b)
d, x, y = gcdC(a,b)
print(d,' = ',a,' * ',x,' + ', b, ' * ',y) 