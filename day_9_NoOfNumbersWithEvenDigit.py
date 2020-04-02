#Given an array nums of integers, return how many of them contain an even number of digits.
#Input: nums = [12,345,2,6,7896]
#Output: 2




def findNumbers(nums):
        mainCount=0
        for i in nums:
            if(len(str(i))%2==0):
                mainCount+=1
        return mainCount

nums=[22,45,678,9889]
print(findNumbers(nums))