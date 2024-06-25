list1 = []
for n in range(100, 1001):
    if n % 7 == 0 and n % 9 == 0:
        list1.append(n)
        print(n)

# If you also want to print the entire list at the end:
print("Numbers between 100 and 1000 divisible by both 7 and 9:", list1)
