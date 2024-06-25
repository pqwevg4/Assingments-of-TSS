n = int(input("Just enter a number between 600 and 800: "))
j = 0

if n < 600 or n > 800:
    print("Follow instructions!")
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            j = 1
            break  # Exit the loop as soon as a divisor is found
    if j == 1:
        print("Not prime")
    else:
        print("Prime")
