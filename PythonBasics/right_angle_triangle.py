try:
    n = int(input("Enter the number: "))  # Prompt user to enter a number
    for i in range(1, n+1):  # Loop from 1 to the entered number
        print('*'* i)  # Print '*' character repeated 'i' times
except ValueError as e:
    # If ValueError occurs (when user enters non-integer input)
    print("Exception:", e)