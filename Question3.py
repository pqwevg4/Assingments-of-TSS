# Define sets S1 and S2
S1 = {10, 20, 30, 40, 50, 60}
S2 = {40, 50, 60, 70, 80, 90}

# (i) Add 55 and 66 in Set S1
S1.add(55)
S1.add(66)
print(f"S1 after adding 55 and 66: {S1}")

# (ii) Remove 10 and 30 from Set S1
S1.discard(10)
S1.discard(30)
print(f"S1 after removing 10 and 30: {S1}")

# (iii) Check whether 40 is present in S1
check_40_in_S1 = 40 in S1
print(f"Is 40 present in S1? {check_40_in_S1}")

# (iv) Find the union between S1 and S2
union_S1_S2 = S1.union(S2)
print(f"Union of S1 and S2: {union_S1_S2}")

# (v) Find the intersection between S1 and S2
intersection_S1_S2 = S1.intersection(S2)
print(f"Intersection of S1 and S2: {intersection_S1_S2}")

# (vi) Find the difference S1 - S2
difference_S1_S2 = S1 - S2
print(f"Difference of S1 - S2: {difference_S1_S2}")
