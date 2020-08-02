'''
Given a number N, return a string consisting of "0"s and "1"s that represents its value in base -2 (negative two).

The returned string must have no leading zeroes, unless the string is "0".

 

Example 1:

Input: 2
Output: "110"
Explantion: (-2) ^ 2 + (-2) ^ 1 = 2
Example 2:

Input: 3
Output: "111"
Explantion: (-2) ^ 2 + (-2) ^ 1 + (-2) ^ 0 = 3


'''
def baseNeg2(N):
    n = N
    if not n: return '0'
    
    ret_val = ''
    state = False
    while n:
        if(n%2 == 0):
            ret_val = '0' + ret_val
        else:
            ret_val = '1' + ret_val
            if state: n += 1 
        n = n // 2
        state = not state 
    return ret_val
N = 2
print(baseNeg2(N))