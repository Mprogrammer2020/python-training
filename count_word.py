'''
Task: Take a user input and count the number of appearances of each alphabets
Example: user_input = "abhishek"
Output: 
a = 1
b = 1
h = 2
i = 1
s = 1
e = 1
k = 1
'''


user_input = input("Enter a string: ")

# Initialize a dictionary to store the count of each alphabet
counts = {}

# Iterate through each character in the string
for char in user_input:
    # Check if the character is an alphabet
    if char.isalpha():
        # If the character is not already in the dictionary, add it with a count of 1
        if char not in counts:
            counts[char] = 1
        # If the character is already in the dictionary, increment its count
        else:
            counts[char] += 1

# Print the count of each alphabet
for char, count in counts.items():
    print(f"{char} = {count}")




