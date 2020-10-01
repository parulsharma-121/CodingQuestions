'''
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.

'''
def firstUniqChar(s):
    freq = {}
    for i in s:
        if(i not in freq):
            freq[i] = 1
        else:
            freq[i] += 1
    
    for i, j in enumerate(s):
        if(freq[j] == 1):
            return i
    return -1
s = "helloworld"
print(firstUniqChar(s))