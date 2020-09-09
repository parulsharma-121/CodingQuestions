'''
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.

'''
def trailingZeroes(n):
    zeros=0
    while(n>4):
        zeros=zeros+int(n/5)
        n=n/5
    
    return zeros
n = 3
print(trailingZeroes(n))