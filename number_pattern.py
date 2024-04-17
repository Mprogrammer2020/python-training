# user to enter a number
n = int(input("Enter the number: "))

# Outer loop 
for i in range(n):
    # Inner loop 
    for j in range(i+1):
        # Print the value of j+1 with  space
        print(j+1, end=" ")
    # new line after print the number for the new  row
    print()


'''
Task: Print the given pattern with single loop
Output:
1
22
333
4444
55555
'''