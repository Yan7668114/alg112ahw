def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]

while True:
    n = int(input("请输入要生成的 Fibonacci 数列的项数 (输入负数退出程序): "))
    
    if n < 0:
        print("程序退出。")
        break
    
    if n < 2:
        print("请输入一个大于等于2的整数。")
        continue
    
    print("前", n, "项的 Fibonacci 数列:")
    for i in range(n):
        print(fibonacci(i), end=" ")
    print("\n")
