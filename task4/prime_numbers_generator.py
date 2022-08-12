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


if __name__ == "__main__":
    print([num for num in prime_generator(100)])
