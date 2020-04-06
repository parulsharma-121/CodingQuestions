'''
For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

Return the largest string X such that X divides str1 and X divides str2.

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
'''


from typing import List
def gcdOfStrings(str1: str, str2: str) -> str:
        if((str1+str2)!=(str2+str1)):
            return ""
        l1=len(str1)
        l2=len(str2)
        while(l1!=l2):
            if(l1>l2):
                l1-=l2
            else:
                l2-=l1
        return str1[:l1]

str1 = "ABCABC"
str2 = "ABC"
print(gcdOfStrings(str1,str2))