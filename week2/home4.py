def twoSum(nums, target):
    flag = None
    result = []
    mapDic = {}
    for idx, ele in enumerate(nums):
        mapDic[ele] = idx
    for i in range(0, len(nums)):
      flag = target - nums[i]
      print(flag)
      if mapDic.get(flag):
        result.append(i)
        result.append(mapDic.get(flag))
        break
    return result
result = twoSum([2, 11, 7, 15], 9)
print(result)
