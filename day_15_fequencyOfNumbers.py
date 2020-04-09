'''
Count Frequency of elements in given array of integers
'''


def frequency(arr):
    freq = dict()
    for x in arr:
        if(x in freq):
            freq[x] += 1
        else:
            freq[x] = 1

    return freq


arr = [1,2,3,4,5,2,4,1,5,2,7,4,8,1,9]
freq = frequency(arr)
for x in freq.keys():
    print(str(x) + " : "+str(freq[x]))
