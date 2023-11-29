def evaluate_polynomial(coefficients, x):
    result = 0
    for i, coeff in enumerate(reversed(coefficients)):
        result += coeff * (x ** i)
    return result

def bisection_method(coefficients, a, b, tolerance=1e-6, max_iterations=1000):
    if evaluate_polynomial(coefficients, a) * evaluate_polynomial(coefficients, b) > 0:
        print("在給定區間內無法保證根的存在")
        return None

    iteration = 0
    while (b - a) / 2 > tolerance and iteration < max_iterations:
        c = (a + b) / 2
        if evaluate_polynomial(coefficients, c) == 0:
            return c
        elif evaluate_polynomial(coefficients, c) * evaluate_polynomial(coefficients, a) < 0:
            b = c
        else:
            a = c
        iteration += 1

    return (a + b) / 2

coefficients = list(map(float, input("請輸入多項式方程式的係數，以空格分隔（從高次到低次）: ").split()))

a = float(input("輸入搜尋區間的左邊界 a: "))
b = float(input("輸入搜尋區間的右邊界 b: "))

result = bisection_method(coefficients, a, b)

if result is not None:
    print("方程式的實數根為:", result)
