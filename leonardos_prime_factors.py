def primeCount(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]   
    
    p = 1
    i = 0
    
    while True:
      p *= primes[i]
      if p > n:
        return i
      i += 1
    
    return 0

n = 11

print(primeCount(n))