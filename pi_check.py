import random
import multiprocessing

m = 10
check = 20000
def points(n):
    k = 0
    for i in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x*x + y*y <= 1:
            k += 1
    return k

def test(pool):
    a = pool.map(points, [check]*m)
    return a

if __name__ == '__main__':
    pool = multiprocessing.Pool()
    #print(test(pool))
    k = sum(test(pool))
    print(4 * k/(check*m))