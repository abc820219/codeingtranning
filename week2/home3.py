def maxProduct(nums):  # 請用你的程式補完這個函式的區塊
    one = 0
    two = 0
    flag = None
    for n in nums:
        if n > one:
            flag = one
            one = n
            two = flag
            continue
        if n < one and  n > two:
            print(n)
            two = n
    print(one * two)
maxProduct([5, 20, 2, 6])

#and or