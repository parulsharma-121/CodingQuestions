'''
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

Example 1:
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101
Example 2:
Input: 7
Output: False
Explanation:
The binary representation of 7 is: 111.

'''
def hasAlternatingBits(n):
    s = bin(n)
    for i in range(len(s)-1):
        if(s[i]==s[i+1]):
            return False
    return True
n = 5
print(hasAlternatingBits(n))