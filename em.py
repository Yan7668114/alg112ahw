f = lambda x: x**2 - 3*x + 1

x = 0.0

max_iterations = 100

epsilon = 1e-6

for i in range(max_iterations):
    fx = f(x)

    if abs(fx) < epsilon:
        break

    dfx = 2*x - 3  
    x = x - fx / dfx
print("近似根:", x)
