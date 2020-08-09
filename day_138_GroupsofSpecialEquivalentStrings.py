def numSpecialEquivGroups(A):
    n = len(A)

    odd = [''.join(sorted(a[::2])) for a in A]
    even = [''.join(sorted(a[1::2])) for a in A]
    group = [odd[i] + even[i] for i in range(n)]
    
    return len(set(group))
A = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]
print(numSpecialEquivGroups(A))