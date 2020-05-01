'''
Given a non-negative integer num, 
repeatedly add all its digits until the result has only one digit.

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
'''
from typing import List
def addDigits(num: int) -> int:
    res=0
    while(num>0):
        rem = num%10
        res = res+rem
        num = int(num/10)
    if(res<10):
        return res
    else:
        return addDigits(res)

num = 38
print(addDigits(num))