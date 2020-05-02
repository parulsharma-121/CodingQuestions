'''
The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]


'''
def findErrorNums(nums):
    nums = sorted(nums)
    result = []
    set1 = set(nums)
    set2 = set([ i for i in range(1, len(nums)+1)])
    for i in range(len(nums)-1):
        if(nums[i]==nums[i+1]):
            result.append(nums[i])
            break
            
    result.append(list(set2 - set1)[0])
    print(list(set2-set1)[0])
    
    return result

nums = [1,2,2,4]
print(findErrorNums(nums))