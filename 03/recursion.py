def permutations(nums):
    def backtrack(first):
        if first == len(nums):
            result.append(nums[:])
        for i in range(first, len(nums)):
            nums[first], nums[i] = nums[i], nums[first]
            backtrack(first + 1)
            nums[first], nums[i] = nums[i], nums[first]

    result = []
    backtrack(0)
    return result

user_input = input("請輸入數字序列（以空格分隔）：")
nums = [int(x) for x in user_input.split()]

if len(nums) == 0:
    print("請輸入有效的數字序列。")
else:
    result = permutations(nums)
    for perm in result:
        print(perm)
