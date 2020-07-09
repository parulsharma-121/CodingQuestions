'''
Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 
Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.

 

Example 1:

Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

'''
def freqAlphabets(s):
    res = ''
    i = 0
    while(i<len(s)):
        if((i+2)<len(s) and s[i+2]=='#'):
            ch = chr(int(s[i:i+2])+96)
            res += ch
            i += 3
        else:
            j = int(s[i]) + 96
            res += chr(j)
            i += 1
    return res
s = "10#11#12"
print(freqAlphabets(s))