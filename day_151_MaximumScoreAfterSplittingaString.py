'''
Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

 

Example 1:

Input: s = "011101"
Output: 5 
Explanation: 
All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5 
left = "01" and right = "1101", score = 1 + 3 = 4 
left = "011" and right = "101", score = 1 + 2 = 3 
left = "0111" and right = "01", score = 1 + 1 = 2 
left = "01110" and right = "1", score = 2 + 1 = 3
'''
def maxScore(s):
    max_score = (1 if s[0] == '0' else 0) + s[1:].count('1')
    curr = max_score
    for n in s[1:-1]:
        curr += 1 if n == '0' else -1 
        max_score = max(max_score, curr)
    return max_score
s = "011101"
print(maxScore(s))