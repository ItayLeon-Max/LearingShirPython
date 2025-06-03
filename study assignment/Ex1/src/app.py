#EX1    
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def n_primes(x):
    count = 0
    for num in range(2, x + 1):
        if is_prime(num):
            count += 1
    return count

if __name__=="__main__":
    print(f"{10}, {n_primes(10)}")  # Primes: 2, 3, 5, 7 -> 4
    print(f"{20}, {n_primes(20)}")  # Primes: 2, 3, 5, 7, 11, 13, 17, 19 -> 8
    print(f"{1}, {n_primes(1)}")    # -> 0
    print(f"{2}, {n_primes(2)}")    # -> 1
    print(f"{100}, {n_primes(100)}")  # -> 25