'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

'''

def isAnagram(s, t):
    S=sorted(s)
    T=sorted(t)
    if(S==T):
        return True
    else:
        return False

s = "anagram"
t = "nagaram"
print(isAnagram(s,t))