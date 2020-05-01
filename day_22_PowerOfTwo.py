'''   
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 2^0 = 1
'''

def isPowerOfTwo(n):
    if(n==0):
        return False
    while(n!=1):
        n=n/2
        if(n%2!=0 and n!=1):
            return False
        
    return True


n = 28
print(isPowerOfTwo(n))