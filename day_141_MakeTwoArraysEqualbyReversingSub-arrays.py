'''
Given two integer arrays of equal length target and arr.

In one step, you can select any non-empty sub-array of arr and reverse it. You are allowed to make any number of steps.

Return True if you can make arr equal to target, or False otherwise.

 

Example 1:

Input: target = [1,2,3,4], arr = [2,4,1,3]
Output: true
Explanation: You can follow the next steps to convert arr to target:
1- Reverse sub-array [2,4,1], arr becomes [1,4,2,3]
2- Reverse sub-array [4,2], arr becomes [1,2,4,3]
3- Reverse sub-array [4,3], arr becomes [1,2,3,4]
There are multiple ways to convert arr to target, this is not the only way to do so.



'''
def canBeEqual(target, arr):
    if(len(target) != len(arr)) :
        return False
    else :
        d = {}
        for i in arr :
            if(i in d) :
                d[i]+=1
            else :
                d[i] = 1
        for j in target :
            if(j in d) :
                d[j]-=1
            else :
                d[j] = 1
        for val in d.values() :
            if(val !=0) :
                return False
        return True 
target = [1,2,3,4]
arr = [2,4,1,3]
print(canBeEqual(target,arr))