
from typing import List
def selfDividingNumbers( left: int, right: int) -> List[int]:
    lst=[]
    for i in range(left,right+1):
        for j in str(i):
            if(int(j)==0 or i%int(j)!=0):
                break
        else:
            lst.append(i)
    return lst


left = 1
right = 22
print(selfDividingNumbers(left,right))