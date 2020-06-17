'''
Given an integer n. No-Zero integer is a positive integer which doesn't contain any 0 in its decimal representation.

Return a list of two integers [A, B] where:

A and B are No-Zero integers.
A + B = n
It's guarateed that there is at least one valid solution. If there are many valid solutions you can return any of them.

 

Example 1:

Input: n = 2
Output: [1,1]
Explanation: A = 1, B = 1. A + B = n and both A and B don't contain any 0 in their decimal representation.
 
 '''
def getNoZeroIntegers(n):
    for i in range(n):
        j = n - i
        if (not '0' in str(i) and not '0' in str(j)):
            return [i, j]
n = 2
print(getNoZeroIntegers(n))