#Task 1 modification tuple
#Given Data
tup = (10, 20, 30, 40, 50)

# Adding 60 to the tuple
new_tup = tup + (60,) # Here you have assigned a tuple to a new variable, modify the existing tuple i.e tup
print(new_tup)

# Removing 50 from the tuple
t = (10, 20, 30, 40, 50, 60)   # here use the tuple that is being modified
new_t = tuple(x for x in t if x != 50)  # Same for here, modify the existing tuple i.e tup
print(new_t) 

# Replacing an element in the tuple
tup = tuple(list(tup)[:4] + [50] + list(tup)[5:]) # Same for here, modify the existing tuple i.e tup
print(tup)

tup = tup[:-1] # Same for here, modify the existing tuple i.e tup
print(tup)


# Changes that need to be done:
# 1. Add 60 to the existing tuple, don't create a new tuple
# 2. Remove 50 from the existing tuple, don't create a new tuple
# 3. Add 50 to the existing tuple, don't create a new tuple
# 4. Remove 60 from the existing tuple, don't create a new tuple
