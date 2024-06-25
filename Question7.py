D = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}

# Open the file in write mode
with open("Question7.txt", "w") as file:
    # Iterate over the dictionary items
    for key, value in D.items():
        # Write each key-value pair to the file in the desired format
        file.write(f"{key}, {value}\n")

print("Dictionary keys and values have been written to output.txt")
