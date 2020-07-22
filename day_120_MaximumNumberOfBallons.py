'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
'''
def maxNumberOfBalloons(text):
    z='balloon'
    d={'n': 0, 'l': 0, 'a': 0, 'b': 0, 'o': 0}
    for i in text:
        if i in z:
            d[i]+=1
    return min(d['b'],d['a'],d['l']//2,d['o']//2,d['n'])
text = "nlaebolko"
print(maxNumberOfBalloons(text))
        