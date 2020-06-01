'''
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

'''
def validPalindrome(s):
    if(s == s[::-1]):
        return True
    s1 = list(s)
    l = 0
    r = len(s)-1
    while (l < r):
        if(s[l] == s[r]):
            l += 1
            r -= 1
        else:
            temp = s1[l]
            del s1[l]
            if(s1 == s1[::-1]):
                return True
            else:
                s1.insert(l, temp)
                del s1[r]
                if(s1 == s1[::-1]):
                    return True
                else:
                    return False

s = 'aba'
print(validPalindrome(s))