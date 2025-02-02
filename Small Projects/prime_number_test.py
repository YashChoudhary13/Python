def is_prime(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    if len(factors) > 2 or len(factors) < 2:
        print(f"{num} is not prime")
    else:
        print(f"{num} is prime")

number = int(input())
is_prime(number)