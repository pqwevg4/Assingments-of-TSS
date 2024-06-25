import random

# Generate two lists of 10 random numbers each between 10 and 30
list1 = [random.randint(10, 30) for _ in range(10)]
list2 = [random.randint(10, 30) for _ in range(10)]

# Print the generated lists
print(f"List 1: {list1}")
print(f"List 2: {list2}")

# Find common numbers using set intersection
common_nums = list(set(list1) & set(list2))
print(f"Common Numbers: {common_nums}")

# Find unique numbers using symmetric difference
unique_nums = list(set(list1).symmetric_difference(set(list2)))
print(f"Unique Numbers: {unique_nums}")

# Find minimum and maximum in both lists
min_list1 = min(list1)
max_list1 = max(list1)
min_list2 = min(list2)
max_list2 = max(list2)

print(f"Minimum in List 1: {min_list1}, Maximum in List 1: {max_list1}")
print(f"Minimum in List 2: {min_list2}, Maximum in List 2: {max_list2}")

# Calculate the sum of both lists
sum_list1 = sum(list1)
sum_list2 = sum(list2)

print(f"Sum of List 1: {sum_list1}")
print(f"Sum of List 2: {sum_list2}")
