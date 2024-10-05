numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for coat in numbers:
    if coat == 1:
        continue
    is_prime = True
    for i in range (2, coat):
        if coat % i == 0:
            is_prime = False
    if is_prime:
        primes.append(coat)
    else:
        not_primes.append(coat)
print (primes)
print (not_primes)