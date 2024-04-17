user_input = (input("enter the few words: "))
letter_count = {letter: user_input.count(letter) for letter in user_input}


# Output the counts
for letter, count in letter_count.items():
    print(f"{letter} = {count}")


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


'''Do your coding here again with understanding'''
