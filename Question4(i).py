import random
import string

# Function to generate a random string of a given length
def generate_random_string(length):
    # Define the possible characters in the string
    characters = string.ascii_letters
    # Use random.choices to generate a random string
    random_string = ''.join(random.choices(characters, k=length))
    return random_string

# Number of random strings to generate
num_strings = 100
# Length of each random string
string_length = 7

# List to store the random strings
random_strings = []

# Generate the random strings
for _ in range(num_strings):
    random_strings.append(generate_random_string(string_length))

# Print the random strings
for i, s in enumerate(random_strings, 1):
    print(f"{i}: {s}")
