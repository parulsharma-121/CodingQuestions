'''
Rearrange the spaces so that there is an equal number of spaces between every pair of adjacent words and that number is maximized. If you cannot redistribute all the spaces equally, place the extra spaces at the end, meaning the returned string should be the same length as text.

Return the string after rearranging the spaces.

 

Example 1:

Input: text = "  this   is  a sentence "
Output: "this   is   a   sentence"
Explanation: There are a total of 9 spaces and 4 words. We can evenly divide the 9 spaces between the words: 9 / (4-1) = 3 spaces.
Example 2:

Input: text = " practice   makes   perfect"
Output: "practice   makes   perfect "
Explanation: There are a total of 7 spaces and 3 words. 7 / (3-1) = 3 spaces plus 1 extra space. We place this extra space at the end of the string.

'''
def reorderSpaces(text):
    spaces = text.count(' ')
    words = text.split()
    if(len(words)==1):
        return words[0] + (' ' * spaces)
    n = len(words) - 1
    spaces_bw_words = spaces // n
    space_in_end = spaces % n
    return (' '*spaces_bw_words).join(words) + (' ' * space_in_end)
text = "  this   is  a sentence "
print(reorderSpaces(text))