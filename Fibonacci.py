def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]

while True:
    n = int(input("請輸入要生成的 Fibonacci 數列的項數 (輸入負數退出執行): "))
    
    if n < 0:
        print("退出執行。")
        break
    
    if n < 2:
        print("請輸入一個大於等於2的整數。")
        continue
    
    print("前", n, "項的 Fibonacci 數列:")
    for i in range(n):
        print(fibonacci(i), end=" ")
    print("\n")
