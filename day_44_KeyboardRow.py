'''
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
 
Example:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]

'''
def findWords(words):
    s1 = "qwertyuiop"
    s2 = "asdfghjkl"
    s3 = "zxcvbnm"
    result = []
    myHash = dict()
    for i in words:
        for x in i:
            if (x.lower() in s1):
                myHash[x] = 1
            elif (x.lower() in s2):
                myHash[x] = 2
            else:
                myHash[x] = 3
    for word in words:
        temp = myHash[word[0]]
        sameRow = True
        for i in word:
            if myHash[i] != temp:
                sameRow = False
                break
        if sameRow:
            result.append(word)

    return result
input = ["Hello", "Alaska", "Dad", "Peace"]
print(findWords(input))