''' Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

'''


def reverseString(S):
        s=list(S)

        l=0
        r=len(s)-1
        while(l<r):
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
            
        return ''.join(s)

S="helloworld"
print(reverseString(S))
        