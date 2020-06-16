def isPrefixOfWord(sentence, searchWord):
    myList = sentence.split(' ')
    for i in range(len(myList)):
        if searchWord in myList[i][0:len(searchWord)]:
            return i+1
    return -1
sentence = "i love eating burger"
searchWord = "burg"
print(isPrefixOfWord(sentence,searchWord))