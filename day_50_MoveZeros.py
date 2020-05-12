'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]


'''
def moveZeroes(nums):
    x = 0
    for i in range(len(nums)):
        if (nums[x] == 0):
            nums.append(nums.pop(x))
            x = x-1
        x += 1
    return nums
nums = [0,1,0,3,12]
print(moveZeroes(nums))