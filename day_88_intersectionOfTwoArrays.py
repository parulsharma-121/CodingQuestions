'''
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]


'''
def intersection(nums1, nums2):
    res = set()
    for i in nums1:
        if(i in nums2):
            res.add(i)

    return res
nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersection(nums1,nums2))
                