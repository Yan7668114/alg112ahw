def power2n_method1(n):
    result = 2**n
    print(f"2^{n} = {result}")
    return result

def power2n_method2a(n):
    def recursive_power2n(n):
        if n == 0:
            result = 1
        else:
            result = recursive_power2n(n - 1) + recursive_power2n(n - 1)
        return result
    
    result = recursive_power2n(n)
    print(f"2^{n} = {result}")
    return result

def power2n_method2b(n):
    def recursive_power2n(n):
        if n == 0:
            result = 1
        else:
            result = 2 * recursive_power2n(n - 1)
        return result
    
    result = recursive_power2n(n)
    print(f"2^{n} = {result}")
    return result

def power2n_method3(n, memo={}):
    def recursive_power2n(n):
        if n in memo:
            result = memo[n]
        elif n == 0:
            result = 1
        else:
            result = 2 * recursive_power2n(n - 1)
            memo[n] = result
        return result
    
    result = recursive_power2n(n)
    print(f"2^{n} = {result}")
    return result

while True:
    method = input("請選擇方法 (1/2a/2b/3)，或輸入 'q' 退出執行:")

    if method == 'q':
        print("退出。")
        break

    n = int(input("请输入 n 的值: "))

    if method == '1':
        power2n_method1(n)
    elif method == '2a':
        power2n_method2a(n)
    elif method == '2b':
        power2n_method2b(n)
    elif method == '3':
        power2n_method3(n)
    else:
        print("無效的方法選擇，請重新輸入。")
