def maxProduct(nums):  # 請用你的程式補完這個函式的區塊
    result = 0
    if len(nums) == 0:
        return  print(result)
    if len(nums) == 2:
        result = nums[0] * nums[1]
        return  print(result)
    if len(nums) == 1:
        result = nums[0]
       
        return  print(result)
    for i in range(0,len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] * nums[j] > result:
                result = nums[i] * nums[j]
    print(result)

maxProduct([2])
maxProduct([10, 2])
maxProduct([-10, 2])
maxProduct([5, 20, 2, 6])
maxProduct([10, -20, 0, 3])
maxProduct([-10, -20, 3, 4])