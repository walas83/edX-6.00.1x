def genPrimes():
    primes = []
    x = 2 
    while True:
        prime = True
        for p in primes:
            if (x % p) == 0:
                prime = False
                break
        if prime:
            yield x
            primes.append(x)
        x += 1
            
            
aaa = genPrimes()
print aaa
print aaa.next()
print aaa.next()
print aaa.next()
print aaa.next()