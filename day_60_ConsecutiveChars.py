'''
Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.

 

Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.
Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

'''
def maxPower(s):
    first = s[0]
    ans = 1
    current = 1
    for i in s[1:]:
        if(i==first):
            current += 1
            ans = max(current,ans)
        else:
            current = 1
        first = i
    return ans

s = "leetcode"
print(maxPower(s))