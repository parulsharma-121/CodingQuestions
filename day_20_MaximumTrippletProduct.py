'''
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:

Input: [1,2,3]
Output: 6

'''


def maximumProduct(nums):
    prod = 1
    lst = []
    for i in nums:
        if (i >= 0):
            lst.append(i)
    lst1 = sorted(lst, reverse=True)
    i = 0
    while (i < 3):
        prod = prod * lst1[i]
        i += 1
    return prod


nums = [-1,-2,7,8,2,-3]
print(maximumProduct(nums))
