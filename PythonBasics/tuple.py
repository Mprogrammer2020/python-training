# Given tuple
tup = (10, 20, 30, 40, 50)

print(tup)  # Output: (10, 20, 30, 40, 50)

# Adding new element into the tuple
tup = list(tup)
tup.append(60)
tup = tuple(tup)
print(tup)  # Output: (10, 20, 30, 40, 50, 60)

# Removing element 50 from the list
tup = list(tup)
tup.remove(50)
tup = tuple(tup)
print(tup)  # Output: (10, 20, 30, 40, 60)


# Adding element 50 back to the tuple
tup = list(tup)
tup.insert(4,50)
tup = tuple(tup)
print(tup)  # Output: (10, 20, 30, 40, 50, 60)

# Removing element 60 from the list
tup = list(tup)
tup.pop()
tup = tuple(tup)
print(tup)  # Output: (10, 20, 30, 40, 50)
