'''
Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).

You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.

Return the reformatted string or return an empty string if it is impossible to reformat the string.

 

Example 1:

Input: s = "a0b1c2"
Output: "0a1b2c"
Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.

'''
def reformat(s):
    res = ''
    a = []
    b = []
    for i in s:
        if(ord(i)>=97 and ord(i)<=123):
            a.append(i)
        else:
            b.append(i)
    if abs(len(a)-len(b))<=1:
        while(a and b):
                res += a.pop()
                res += b.pop()
        if(a):
            res += a.pop()
        if(b):
            res = b.pop()+res
            
    return res   
s = "a0b1c2"
print(reformat(s))