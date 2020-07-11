'''
Alice and Bob have candy bars of different sizes: A[i] is the size of the i-th bar of candy that Alice has, and B[j] is the size of the j-th bar of candy that Bob has.

Since they are friends, they would like to exchange one candy bar each so that after the exchange, they both have the same total amount of candy.  (The total amount of candy a person has is the sum of the sizes of candy bars they have.)

Return an integer array ans where ans[0] is the size of the candy bar that Alice must exchange, and ans[1] is the size of the candy bar that Bob must exchange.

If there are multiple answers, you may return any one of them.  It is guaranteed an answer exists.

 

Example 1:

Input: A = [1,1], B = [2,2]
Output: [1,2]

'''
def fairCandySwap(A, B):
    A.sort()
    B.sort()        
    left = right = 0
    diff = (sum(A) - sum(B)) / 2
    while True:
        temp = A[left] - B[right]
        if temp > diff:
            right += 1
        elif temp < diff:
            left += 1
        else:
            return [A[left], B[right]]
A = [1,1]
B = [2,2]
print(fairCandySwap(A,B))