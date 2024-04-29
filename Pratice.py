'''[1] Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers'''

value = (input("enter the number:  "))
list=value.split(',')
tuple =tuple(list)

print(list,tuple)

'''[2] Write a  Python program that accepts a filename from the user and prints the extension of the file.'''

# Prompt the user to input a filename and store it in the 'filename' variable
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print(f_extns[-1])

# accepts the integer (n) output be like 555
a =int(input("enetr the single any number: "))
n1 =("%s" % a)
n2 =("%s%s" % (a,a))
n3 =("%s%s%s" % (a,a,a))
print(n1 + n2+ n3)


#slice_number
x  = [1,2,3]
y =x[:-1]
z=x
print(z)

#date_time  check
from datetime import date
first_date = date(27,6,5)
sec_date = date(27,5,2)
delta =first_date-sec_date
print(delta.days)

[6] #Write a  Python program to calculate the difference between a given number and 17. 
def reverse_list_in_location(lst, start_pos, end_pos):
    
    while start_pos < end_pos:
        lst[start_pos], lst[end_pos] = lst[end_pos], lst[start_pos]
        start_pos += 1
        end_pos -= 1
    return lst
number=[4,5,6,76,7,8,81,6]
start_pos =2
end_pos =5
print(number)


print(reverse_list_in_location(number, start_pos, end_pos))

#exe[7] write the program diff b/w given numbers 17, if 17 is greater then print twice difference
n=int(input("enetr the number: "))
def diff(n):
    if n<=17:
        return 17-n
    else:
        return(17-n)**2
    
result = diff(n)
print(result)

#[8] write the python near thouansd value

# create function 
n=int(input("enetr the number: "))
def thounasd(n):
    #if n<=100:
        return (abs(1000-n)<=100) or (abs(2000-n)<=100)
result =thounasd(n)
print(result)

'''Write a  Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.'''

# Define a function named "sum_thrice" that takes three integer parameters: x, y, and z
def sum_thrice(x, y, z):
    # Calculate the sum of x, y, and z
    sum = x + y + z
    if x == y == z:
        sum = sum * 3
    return sum
print(sum_thrice(1, 2, 3))

print(sum_thrice(3, 3, 3))



# Define a function named "new_string" that takes a string parameter called "text"
def new_string(text):
    # Check if the length of the "text" is greater than or equal to 2 and if the first two characters of "text" are "Is"
    if len(text) >= 2 and text[:2] == "Is":
        return text
    else:
        return "Is" + text

print(new_string("ArrayIsrtxffffffgxs edrftghj"))

print(new_string("IsEmpty"))

#check odd or even number
n = int(input("enter the number:  "))

if n%2==0:
    print("this is even  number")
elif n%2!=0:
    print("this is odd number")
    
# check the element present in list or not
def ele_check(data_group,n):
    for value in data_group:
        if value==n:
            return True
        return False
  
print(ele_check([3,4,4,5,3,2],6))




    


