"""example of using iterables to first 1000 primes"""

from itertools import islice, count

thousand_primes = islice((x for x in count() if is_prime(x)), 1000)

list(thousand_primes)
