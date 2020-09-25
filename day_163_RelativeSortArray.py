'''
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

 

Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]

'''
def relativeSortArray(arr1, arr2):
    res1=[]
    res2=[]
    for i in arr2:
        for j in range(len(arr1)):
            if(i==arr1[j]):
                res1.append(arr1[j])
    for k in range(len(arr1)):
        if(arr1[k] not in res1):
            res2.append(arr1[k])
    res2.sort()
    return res1+res2
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
print(relativeSortArray(arr1,arr2))        