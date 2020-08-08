'''
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

 

Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.

'''
def repeatedSubstringPattern(s):
    n=len(s)
    for i in range(1,int(n/2)+1):
        if(n%i==0):
            temp=s[0:i]
            result=""
            t=int(n/i)
            for j in range(t):
                result+=temp
            if(result==s):
                return True
    return False
s = "abab"
print(repeatedSubstringPattern(s))
