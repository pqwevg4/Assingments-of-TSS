# Initial list
L = [11, 12, 13, 14]

# (i) Add 50 and 60 to L
L.append(50)
L.append(60)
print(f"List after adding 50 and 60: {L}")

# (ii) Remove 11 and 13 from L
if 11 in L:
    L.remove(11)
if 13 in L:
    L.remove(13)
print(f"List after removing 11 and 13: {L}")

# (iii) Sort L in ascending order
L.sort()
print(f"List sorted in ascending order: {L}")

# (iv) Sort L in descending order
L.sort(reverse=True)
print(f"List sorted in descending order: {L}")

# (v) Search for 13 in L
search_result = "Yes" if 13 in L else "No"
print(f"Is 13 in the list? {search_result}")

# (vi) Count the number of elements present in L
count_elements = len(L)
print(f"Number of elements in the list: {count_elements}")

# (vii) Sum all the elements in L
sum_elements = sum(L)
print(f"Sum of all elements: {sum_elements}")

# (viii) Sum all odd numbers in L
sum_odd = sum(i for i in L if i % 2 != 0)
print(f"Sum of all odd numbers: {sum_odd}")

# (ix) Sum all even numbers in L
sum_even = sum(i for i in L if i % 2 == 0)
print(f"Sum of all even numbers: {sum_even}")

# (x) Sum all prime numbers in L
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

sum_prime = sum(i for i in L if is_prime(i))
print(f"Sum of all prime numbers: {sum_prime}")

# (xi) Clear all the elements in L
L.clear()
print(f"List after clearing all elements: {L}")

# (xii) Delete L
del L
try:
    print(L)
except NameError:
    print("The list L has been deleted.")
