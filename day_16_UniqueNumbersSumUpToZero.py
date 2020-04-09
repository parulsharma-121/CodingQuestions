'''
Given an integer n, return any array containing n unique integers such that they add up to 0.

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

'''


from typing import List
def sumZero(n: int) -> List[int]:
        lst=[]
        if(n==1):
            lst.append(0)
        elif(n%2==0):
            a=n/2
            i=1
            while(i<=a):
                lst.append(i)
                lst.append(-i)
                i+=1
        else:
            lst.append(0)
            a=n/2
            i=1
            while(i<=a):
                lst.append(i)
                lst.append(-i)
                i+=1
        return lst

n=5
print(sumZero(n))