from typing import Generator


def is_prime(n: int) -> bool:
    """Return True if `n` is prime, otherwise False."""
    for num in range(2, n):
        if n % num == 0:
            return False
    return True


def prime_generator(limit: int) -> Generator[int, None, None]:
    """Generator to return prime numbers one by one."""
    for num in range(2, limit):
        if is_prime(num):
            yield num


# ----------------------------------- Sieve of Eratosthenes ----------------------------------------


def prime_generator2(limit: int) -> Generator[int, None, None]:
    """Generator to return prime numbers. Implementation of Sieve of Eratosthenes."""
    arr = [0 if i == 1 else i for i in range(limit)]  # 1 is not prime number
    i = 2
    while i < limit:
        if arr[i] != 0:
            yield arr[i]
            j = 2 * i
            while j < limit:
                arr[j] = 0
                j += i
        i += 1


def prime_generator3(limit: int) -> Generator[int, None, None]:
    """Generator to return prime numbers. Implemented using set difference."""
    sieve = set(range(2, limit))
    while sieve:
        prime = min(sieve)
        yield prime
        sieve -= set(range(prime, limit, prime))


if __name__ == "__main__":
    n = 100
    print([num for num in prime_generator(n)])
    print([num for num in prime_generator2(n)])
    print([num for num in prime_generator3(n)])
