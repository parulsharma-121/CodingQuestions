'''
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000

'''
def findMaxConsecutiveOnes(nums):
    currentLen = 0
    maxLen = 0
    
    for x in nums:
        if (x == 1):
            currentLen += 1
        
        else:
            
            maxLen = max(maxLen, currentLen)
            currentLen = 0
            
    return max(maxLen, currentLen)

nums = [1,1,0,1,1,1]
print(findMaxConsecutiveOnes(nums))