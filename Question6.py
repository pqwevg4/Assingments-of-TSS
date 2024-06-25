import random

# Generate a list of 100 random numbers between 100 and 900
list1 = [random.randint(100, 900) for _ in range(100)]
#print(list1)

# Lists to store odd, even, and prime numbers
odd_nums = []
even_nums = []
prime_nums = []

# Separate odd and even numbers
for num in list1:
    if num % 2 == 0:
        even_nums.append(num)
    else:
        odd_nums.append(num)

# Print even and odd numbers
print(f"Even numbers ({len(even_nums)}): {even_nums}")
print(f"Odd numbers ({len(odd_nums)}): {odd_nums}")

# Find and print prime numbers
for num in list1:
    if num > 1:  # Prime numbers are greater than 1
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_nums.append(num)

print(f"Prime numbers ({len(prime_nums)}): {prime_nums}")
