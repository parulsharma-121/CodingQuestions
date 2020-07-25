'''
Given an array of integers arr.

We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

Let's define a and b as follows:

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Note that ^ denotes the bitwise-xor operation.

Return the number of triplets (i, j and k) Where a == b.

 

Example 1:

Input: arr = [2,3,1,6,7]
Output: 4
Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)


'''
def countTriplets(arr):
    res = total = 0
    for r in range(len(arr)):
        total ^= arr[r]
        temp = total
        for l in range(r):
            if temp == 0:
                res += r - l
            temp ^= arr[l]
    return res
arr = [2,3,1,6,7]
print(countTriplets(arr))