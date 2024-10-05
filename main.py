numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for count in numbers:
    if count == 1:
        continue
    is_prime = True
    for i in range (2, count):
        if count % i == 0:
            is_prime = False
    if is_prime:
        primes.append(count)
    else:
        not_primes.append(count)
print (primes)
print (not_primes)