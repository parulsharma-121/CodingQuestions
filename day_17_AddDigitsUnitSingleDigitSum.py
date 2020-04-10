
from typing import List
def addDigits(num: int) -> int:
    res=0
    while(num>0):
        rem = num%10
        res = res+rem
        num = int(num/10)
    if(res<10):
        return res
    else:
        return addDigits(res)

num = 38
print(addDigits(num))