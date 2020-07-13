'''
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.

'''
def numIdenticalPairs(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if(nums[i]==nums[j]):
                count += 1
    return count
nums = [1,2,3,1,1,3]
print(numIdenticalPairs(nums))