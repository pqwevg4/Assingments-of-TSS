import random
import time
start_time = time.time()

# Generate a list of n random integers between 1 and 10000
elements = [random.randint(1, 10000) for _ in range(25000)]

# Sort the list in ascending order using sorted() function
sorted_elements = sorted(elements)

# Print the sorted list
print("Sorted elements:")
print(sorted_elements)
end_time = time.time()
final_time = (end_time - start_time)
print(f"The final time elapsed is : {final_time :.2f} seconds !")