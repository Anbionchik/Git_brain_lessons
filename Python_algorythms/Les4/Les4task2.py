import cProfile

def sieve(n):


    primes_list = [2]
    number = 3

    while len(primes_list) < n:
        skip = False
        for i in primes_list:
            if not number % i:
                skip = True
                break
        if skip:
            number += 1
            continue
        else:
            for i in range(primes_list[-1], int(number**0.5)):
                if not number % i:
                    skip = True
                    break
        if skip:
            number += 1
            continue
        else:
            primes_list.append(number)

    return primes_list[-1]


def primes(n):

    primes_list = []
    number = 2
    while len(primes_list) < n:
        complex = False
        for i in range(2, number):
            if not number % i:
                complex = True
                break
        if not complex:
            primes_list.append(number)
        number +=1

    return primes_list[-1]


# cProfile.run('primes(100)')
# print(sieve(2000))
# print(primes(2000))

