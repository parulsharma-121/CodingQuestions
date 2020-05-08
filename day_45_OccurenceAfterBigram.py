'''
Given words first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.

For each such occurrence, add "third" to the answer, and return the answer.

 

Example 1:

Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
Output: ["girl","student"]
Example 2:

Input: text = "we will we will rock you", first = "we", second = "will"
Output: ["we","rock"]

'''
def findOcurrences(text, first, second):
    Text = text.split()
    i = 0
    result = []
    while(i<len(Text)-2):
        j = i+1
        k = j+1
        if(Text[i] == first and Text[j] == second):
            result.append(Text[k])
        i += 1
    return result

text = "alice is a good girl she is a good student"
f = "a"
s = "good"
print(findOcurrences(text,f,s))