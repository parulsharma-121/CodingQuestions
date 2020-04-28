'''
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.

 

Example 1:

Input: [1,2,2,3]
Output: true


'''
def isMonotonic(A):
    if(A==sorted(A) or A==sorted(A, reverse=True)):
        return True
    return False

A = [1,1,2,4,5]
print(isMonotonic(A))