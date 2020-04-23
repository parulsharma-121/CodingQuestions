'''
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

'''
def countPrimes(n):
    if(n<=2):return 0
    primes = [True]*(n)
    primes[0]=False
    primes[1]=False
    count = 0
    for i in range(2,n):
        if(primes[i]==True):
            count +=1
            j=2
            while((j*i)<n):
                primes[j*i]=False
                j +=1
    
    
    
    return count
n = 10 
print(countPrimes(n))