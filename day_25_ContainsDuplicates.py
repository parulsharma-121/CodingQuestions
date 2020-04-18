'''
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true

'''
def containsDuplicate(nums):
    freq=dict()
    for i in nums:
        if(i in freq):
            freq[i]+=1
        else:
            freq[i]=1
    for i in freq.keys():
        if(freq[i]>1):
            return True
        
nums=[1,2,1,3,4,5,62,4,5]
print(containsDuplicate(nums))