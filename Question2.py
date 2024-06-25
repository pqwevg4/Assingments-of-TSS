# Initialize the dictionary
D = {1: 5.6, 2: 7.8, 3: 6.6, 4: 8.7, 5: 7.7}

# (i) Add new entry in D; key=8 and value is 8.8
D[8] = 8.8
print(f"Dictionary after adding (8, 8.8): {D}")

# (ii) Remove key=2 from D
if 2 in D:
    del D[2]
print(f"Dictionary after removing key=2: {D}")

# (iii) Check whether key=6 is present in D
key_check = 6 in D
print(f"Is key=6 present in the dictionary? {key_check}")

# (iv) Count the number of elements present in D
num_elements = len(D)
print(f"Number of elements in the dictionary: {num_elements}")

# (v) Add all the values present in D
sum_values = sum(D.values())
print(f"Sum of all values in the dictionary: {sum_values}")

# (vi) Update the value of key=3 to 7.1
D[3] = 7.1
print(f"Dictionary after updating key=3 to 7.1: {D}")

# (vii) Clear the dictionary
D.clear()
print(f"Dictionary after clearing: {D}")
