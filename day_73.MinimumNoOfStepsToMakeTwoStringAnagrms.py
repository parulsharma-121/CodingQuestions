'''
Given two equal-size strings s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

 

Example 1:

Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.

'''
def minSteps(s,t):
    count=0
    freq={}
    for i in s:
        if(i in freq):
            freq[i]+=1
        else:
            freq[i]=1
    for j in t:
        if (j in freq):
            if(freq[j]==0):
                count+=1
            else:
                freq[j]-=1
        else:
            count+=1
    return count

s = "bab"
t = "aba"
print(minSteps(s,t))
        