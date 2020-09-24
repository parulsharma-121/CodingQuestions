'''
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false

'''
def uniqueOccurrences(arr):
    freq = dict()
    for i in arr:
        if(i in freq):
            freq[i] += 1
        else:
            freq[i] = 1
    for i in freq:
        if(len(set(freq.values()))==len(freq.values())):
            return True
        return False
arr = [1,2,2,1,1,3]
print(uniqueOccurrences(arr))