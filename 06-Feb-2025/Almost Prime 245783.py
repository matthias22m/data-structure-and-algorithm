# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

def is_prime(n):
    if n <= 1:
        return False
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True

def generate_prime(num):
    primes = set()
    i = 0
    while i <= num:
        if is_prime(i):
            primes.add(i)
        i+=1
    return primes

def solve(num):
    prime_set = generate_prime(num)

    if num < 6:
        return 0
    almost_primes = 0
    
    for n in range(6,num+1):
        count = 0
        for i in range(1,num+1):
            if n%i==0 and i in prime_set:
                count += 1
            if count>2:
                break
        else:
            if count == 2:
                almost_primes+=1
    return almost_primes
num = int(input())
print(solve(num))
            
