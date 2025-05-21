def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(start, end):
    """Generate all prime numbers between start and end (inclusive)."""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Example usage
if __name__ == "__main__":
    # Test the function
    start_num = 300
    end_num = 1000
    result = generate_primes(start_num, end_num)
    print(f"Prime numbers between {start_num} and {end_num}:")
    print(result) 