import itertools


def primes():
    i = 2
    while True:
        r = int(i / 2) + 1 if int(i / 2) > 2 else i
        for v in range(2, r):
            if i % v == 0 and v != i:
                break
        else:
            yield i
        i += 1


print(list(itertools.takewhile(lambda x: x <= 31, primes())))
