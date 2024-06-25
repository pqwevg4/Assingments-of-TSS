import random as r
import string as s

def random_str_generator(length):
    strings = s.ascii_letters
    random_string = "".join(r.choice(strings) for _ in range(length))
    return random_string

with open("Question9.txt", "w") as file:
    no_of_strs = 100
    random_str = []
    for _ in range(no_of_strs):
        str_length = r.randint(10, 15)  # Generate a random length between 10 and 15
        random_str.append(random_str_generator(str_length))
    
    for i, string in enumerate(random_str, 1):
        file.write(f"{i}: {string}\n")

print("100 random strings have been written to Question9.txt")