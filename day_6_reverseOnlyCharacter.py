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