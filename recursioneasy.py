from itertools import permutations

user_input = input("請輸入數字序列（以空格分隔）：")
nums = [int(x) for x in user_input.split()]

if len(nums) == 0:
    print("請輸入有效的數字序列。")
else:
    result = list(permutations(nums))
    for perm in result:
        print(perm)
