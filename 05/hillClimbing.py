import random

def neighbor(f, p, h=0.01):
    x, y, z = p
    x1 = x + random.uniform(-h, h)
    y1 = y + random.uniform(-h, h)
    z1 = z + random.uniform(-h, h)
    return [x1, y1, z1], f(x1, y1, z1)

def hillClimbing(f, p, h=0.01):
    failCount = 0
    while (failCount < 10000):
        x, y, z = p 
        fnow = f(x, y, z)  
        p1, f1 = neighbor(f, [x, y, z], h)  
        if f1 >= fnow:
            fnow = f1
            p = p1
            print('p=', p, 'f(p)=', fnow)
            failCount = 0
        else:
            failCount = failCount + 1
    return (p, fnow)

def f(x, y, z):
    return -1 * (x**2 + y**2 + z**2)

hillClimbing(f, [2, 1, 3])
