'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
find the one that is missing from the array.
Input: [3,0,1]
Output: 2
'''
from typing import List 
def missingNumber(nums: List[int]) -> int:
    nums.sort()
    l=0
    r=len(nums)
    while(l<r):
        m = l+ (r-l)//2
        if nums[m]>m:
            r = m
        else:
            l = m+1
    return l

nums=[0,3,1]
print(missingNumber(nums))