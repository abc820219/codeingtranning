def maxProduct(nums):  # 請用你的程式補完這個函式的區塊
    one = 0
    two = 0
    result = 0
    for i in range(0,len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] * nums[j] > result:
                result = nums[i] * nums[j]
    print(result)


maxProduct([5, 20, 2, 6])
maxProduct([10, -20, 0, 3])
maxProduct([-10, -20, 3, 4])

# and or
