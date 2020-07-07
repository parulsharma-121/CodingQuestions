'''
Given an array of numbers arr. A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Return true if the array can be rearranged to form an arithmetic progression, otherwise, return false.

 

Example 1:

Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.
Example 2:

Input: arr = [1,2,4]
Output: false
Explanation: There is no way to reorder the elements to obtain an arithmetic progression.

'''
def canMakeArithmeticProgression(arr):
    arr.sort()
    n = len(arr)
    d = arr[1]-arr[0]
    for x in range(0,n-1):
        if(d!=arr[x+1]-arr[x]):
            return False
    return True
arr = [3,5,1]
print(canMakeArithmeticProgression(arr))