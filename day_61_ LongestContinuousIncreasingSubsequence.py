def findLengthOfLCIS(nums):
    prev = nums[0]
    res = 1
    current = 1
    for i in nums[1:]:
        if(i>prev):
            current += 1
            res = max(res,current)
        else:
            current = 1
        prev = i
    return res

nums = [1,2,3,4,0,4]
print(findLengthOfLCIS(nums))