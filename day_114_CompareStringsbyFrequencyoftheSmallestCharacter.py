'''
Let's define a function f(s) over a non-empty string s, which calculates the frequency of the smallest character in s. For example, if s = "dcce" then f(s) = 2 because the smallest character is "c" and its frequency is 2.

Now, given string arrays queries and words, return an integer array answer, where each answer[i] is the number of words such that f(queries[i]) < f(W), where W is a word in words.

 

Example 1:

Input: queries = ["cbd"], words = ["zaaaz"]
Output: [1]
Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").

'''
def numSmallerByFrequency(queries, words):
    arr1 = []
    arr2 = []
    for i in words:
        arr2.append(i.count(min(i)))
    for i in queries:
        arr1.append(i.count(min(i)))
    res = []
    for i in arr1:
        count = 0
        for j in arr2:
            if i < j:
                count += 1
        res.append(count)
    return res
queries = ["cbd"]
words = ["zaaaz"]
print(numSmallerByFrequency(queries,words))