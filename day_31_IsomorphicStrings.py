'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false

'''

def isIsomorphic(s, t):
    freq = dict()
    for i in range(len(s)):
        if s[i] in freq:
            if freq[s[i]] != t[i]:
                return False
        elif t[i] in freq.values():
            return False
        else:
            freq[s[i]] = t[i]
    return True

s = "egg"
t = "add"
print(isIsomorphic(s,t))