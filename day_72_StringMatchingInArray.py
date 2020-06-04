'''
Given an array of string words. Return all strings in words which is substring of another word in any order. 

String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j].

 

Example 1:

Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.

'''
def stringMatching(words):
    words.sort(key = len)
    ans = []
    for i in range(len(words)):
        for j in range(i,len(words),1):
            if(i!=j):
                if(words[i] in words[j]):
                    ans.append(words[i])
                    break
    return ans
        
words = ["mass","as","hero","superhero"]
print(stringMatching(words))