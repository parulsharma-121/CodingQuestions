'''
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537

'''
def tribonacci(n):
    if(n == 0):
        return 0
    if(n == 1 or n == 2):
        return 1
    arr = [0] * (n + 1)
    arr[0] = 0
    arr[1] = 1
    arr[2] = 1

    for i in range(3, n + 1):
        arr[i] = arr[i - 3] + arr[i - 2] + arr[i - 1]

    return arr[n]
n = 4
print(tribonacci(n))