# 21.Write a function to check for prime numbers.

def is_prime(n):
    """Efficiently checks if a number is prime."""
    if n <= 3:
        return n > 1  # Only 2 and 3 are primes
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check from 5 to sqrt(n), skipping multiples of 2 and 3
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
print(is_prime(2))