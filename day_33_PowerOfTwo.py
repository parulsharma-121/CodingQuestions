'''
Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false

'''
def isPowerOfThree(n):
    if(n==1):
        return True
    while(n>0):
        n = n/3
        if(n==1):
            return True
    return False

n = 27
print(isPowerOfThree(n))