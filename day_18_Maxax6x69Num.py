'''
Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

Input: num = 9669
Output: 9969
Explanation: 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666. 
The maximum number is 9969.
'''
from typing import List
def maximum69Number (num: int) -> int:
    lst=[int(i) for i in str(num)]
    i=0
    while(i<len(lst)):
        if(lst[i]!=9):
            lst[i]=9
            break;
        i+=1
        
    return int(''.join(map(str,lst)))

num=9969
print(maximum69Number(num))