'''
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

'''
def countBinarySubstrings(s):
    n=len(s)
    if(n<1): return 1
    curr = s[0]
    c1 = 0
    c2 = 0
    i = 0
    res = 0
    while(i<n):
        while(i<n and s[i]==curr):
            i+=1
            c1+=1
        else:
            res+=min(c1,c2)
            if (i<n):
                curr=s[i]
                c2=c1
                c1=0
    return res
s = "00110011"
print(countBinarySubstrings(s))
        