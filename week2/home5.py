def maxZeros(nums):
    result = 0
    for i in range(len(nums)):
        count = 0
        if nums[i] == 0:
            for j in range(i, len(nums)):
               if nums[j] == 0:
                    count = count + 1
               else:
                    break
        if count > result:
            result = count
    return result

result = maxZeros([1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0])

print(result)
