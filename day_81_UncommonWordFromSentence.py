'''
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words. 

You may return the list in any order.

 

Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]

'''
def uncommonFromSentences(A, B):
    c=(A + ' ' + B).split(' ')
    freq={}
    res=[]

    for i in c:
        if(i not in freq):
            freq[i]=1
        else:
            freq[i]+=1
        
    for key,value in freq.items():
        if (value==1):
            res.append(key)
        
    return res
A = "this apple is sweet"
B = "this apple is sour"
print(uncommonFromSentences(A,B))