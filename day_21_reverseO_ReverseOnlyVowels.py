'''Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"'''
from typing import List
def reverseVowels(s: str) -> str:
        s1=["A","E","I","O","U","a","e","i","o","u"]
        lst = list(s)
        l=0
        r=len(lst)-1
        while(l<r):
            if(not lst[l] in s1):
                l+=1
            elif(not lst[r] in s1):
                r-=1
            else:
                lst[l],lst[r]=lst[r],lst[l]
                l+=1
                r-=1
        return "".join(lst)

s="hello"
print(reverseVowels(s))