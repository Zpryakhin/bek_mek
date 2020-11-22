a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
def egcdC(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = egcdC(b, a % b)
        return d, y, x - y * (a // b)
d, x, y = egcdC(a,b)
print(d,' = ',a,' * ',x,' + ', b, ' * ',y) 