'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

'''
def lengthOfLongestSubstring(s):
    empty_str = ''
    length = 0
    for i in s:
        if(i not in empty_str):
            empty_str += i
            length = max(length,len(empty_str))
        else:
            length = max(length,len(empty_str))
            empty_str = empty_str[empty_str.index(i)+1:]
            empty_str += i
    return length
s = "abcdabc"
print(lengthOfLongestSubstring(s))