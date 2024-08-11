def sieve(N):
    is_prime=[True]*(N+1)
    p=2
    while(p*p<=N):
        if is_prime[p]:
            for i in range(p*p,N+1,p):
                is_prime[i]=False
        p=p+1
    primes=[p for p in range(2,N+1) if is_prime[p]]
    return primes

N=int(input())
primes=sieve(N)
for i in primes:
    print(i,end=' ')

#input=10
#output=2 3 5 7 
