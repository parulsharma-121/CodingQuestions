'''
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.

 

Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
Example 2:

Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.

'''
def balancedStringSplit(s):
    rc = lc = c = 0
    for i in s:
        if(i == 'R'):
            rc += 1
        elif(i == 'L'):
            lc += 1
        if (rc == lc):
            rc = lc = 0
            c += 1
    return c
s = "RLRRLLRLRL"
print(balancedStringSplit(s))

        