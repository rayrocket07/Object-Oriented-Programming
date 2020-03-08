def genPrimes():
    prime = 2
    pre_primes = [2]
    while True:
        yield prime
        while True:
            result = []
            prime += 1
            for i in pre_primes:
                result.append(prime % i)
            if 0 in result:
                continue
            pre_primes.append(prime)
            break


