prime_nums = []

for n in range(600, 801):
    is_prime = True
    if n < 2:
        is_prime = False
    else:
        for j in range(2, int(n**0.5) + 1):
            if n % j == 0:
                is_prime = False
                break
    if is_prime:
        prime_nums.append(n)

with open("Question10.txt", "w") as file:
    for prime in prime_nums:
        file.write(f"{prime}\n")