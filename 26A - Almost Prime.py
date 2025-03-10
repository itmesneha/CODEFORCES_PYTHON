import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_almost_prime(n):
    if n <= 3:
        return False
    prime_divisors = set()
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if is_prime(i):
                prime_divisors.add(i)
            if is_prime(n // i):
                prime_divisors.add(n // i)
        if len(prime_divisors) > 2:
            return False
    return len(prime_divisors) == 2

n = int(input())
count_ans = 0
for i in range(1, n + 1):
    if is_almost_prime(i):
        count_ans += 1
print(count_ans)
