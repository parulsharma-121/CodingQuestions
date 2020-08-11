'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4

'''
def searchInsert(nums, target):
    if target > max(nums):
        return len(nums)
    if target < min(nums):
        return 0
    
    # else, if in middle: 
    big = len(nums) - 1
    
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        if nums[i] > target and nums[i] < nums[big]:
            big = i
            
    return big
nums =[1,3,5,6]
target = 5
print(searchInsert(nums,target))