'''
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:

Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
 

Example 2:

Input: 3
Output: False
'''
def judgeSquareSum(c):
    if(int(c**0.5)**2==c):  
        return True
    else:
        for a in range(0,int(c**.5)+1):   
            if int((c-a**2)**0.5)**2==c-a**2:     
                return True     
        return False 
c = 5
print(judgeSquareSum(c))