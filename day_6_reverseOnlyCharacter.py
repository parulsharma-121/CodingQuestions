'''
Given a string S, return the "reversed" string where all
characters that are not a letter stay in the same place,
and all letters reverse their positions.

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

 '''

def reverseOnlyLetters(S: str) -> str:
        lst = list(S)
        l=0
        r=len(lst)-1
        while(l<r):
            if(not lst[l].isalpha()):
                l+=1
            elif(not lst[r].isalpha()):
                r-=1
            else:
                lst[l],lst[r]=lst[r],lst[l]
                l+=1
                r-=1
                
            
            
        return ''.join(lst)

S="Helo-df-sh"
print(reverseOnlyLetters(S))