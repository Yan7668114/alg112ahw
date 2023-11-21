def evaluate_polynomial(coefficients, x):
    """
    计算多项式在给定点 x 处的值
    """
    result = 0
    for i, coeff in enumerate(reversed(coefficients)):
        result += coeff * (x ** i)
    return result

def bisection_method(coefficients, a, b, tolerance=1e-6, max_iterations=1000):
    """
    二分法求解多项式的实数根
    """
    if evaluate_polynomial(coefficients, a) * evaluate_polynomial(coefficients, b) > 0:
        print("在给定区间内无法保证根的存在")
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

# 输入多项式的系数，从高次到低次
coefficients = list(map(float, input("请输入多项式方程的系数，以空格分隔（从高次到低次）: ").split()))

# 输入二分法的搜索区间
a = float(input("输入搜索区间的左边界 a: "))
b = float(input("输入搜索区间的右边界 b: "))

# 调用二分法函数求解
result = bisection_method(coefficients, a, b)

# 输出结果
if result is not None:
    print("方程的实数根为:", result)
