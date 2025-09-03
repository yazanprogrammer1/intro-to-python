import time

# This is my first Python file
print("Hello, World! yazan")
print("I like Python")
print("I love programming")
#Variables = containers for storing data values
my_variable = 10
print(my_variable)
full_name = "John Doe"
age = 30
gpa = 3.5
isStudent = True
print(f"Hello {full_name}")
print(f"Your age is {age}")

if isStudent : print("You are a student")
else : print("You are not a student")

#=========================================== Arithmetic Operators ===========================================
x = 10
y = 3
print(x + y)  # Addition
x += 5  # Increment x by 5
print(x)
print(x - y)  # Subtraction
y -= 2  # Decrement y by 2
print(y)
print(x * y)  # Multiplication
y *= 4  # Multiply y by 4
print(y)
print(x / y)  # Division
x /= 2  # Divide x by 2
print(x)
print(x % y)  # Modulus
y %= 3  # Remainder of y divided by 3
print(y)
print(x ** y) # Exponentiation
x **= 2 # x raised to the power of 2
print(x)
print(x // y) # Floor Division
x //= 3 # Floor divide x by 3
print(x)
#=========================================== Comparison Operators ===========================================
a = 5
b = 10
print(a == b)  # Equal to
print(a != b)  # Not equal to
print(a > b)   # Greater than
print(a < b)   # Less than
print(a >= b)  # Greater than or equal to
print(a <= b)  # Less than or equal to
#=========================================== Logical Operators ===========================================
p = True
q = False
print(p and q)  # Logical AND
print(p or q)   # Logical OR
print(not p)    # Logical NOT
#=========================================== Assignment Operators ===========================================
m = 15
n = 5
m += n  # m = m + n
print(m)
m -= n  # m = m - n
print(m)
m *= n  # m = m * n
print(m)
m /= n  # m = m / n
print(m)
m %= n  # m = m % n
print(m)
m **= n # m = m ** n
print(m)
m //= n # m = m // n
print(m)
#=========================================== Bitwise Operators ===========================================
u = 6  # In binary: 110
v = 3  # In binary: 011
print(u & v)  # Bitwise AND
print(u | v)  # Bitwise OR
print(u ^ v)  # Bitwise XOR
print(~u)     # Bitwise NOT
print(u << 1) # Left shift
print(u >> 1) # Right shift
#=========================================== Membership Operators ===========================================
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)    # True
print(6 not in my_list) # True
#=========================================== Identity Operators ===========================================
a = [1, 2, 3]
b = a
c = a[:]
print(a is b)  # True
print(a is c)  # False
print(a == c)  # True
#=========================================== Control Flow (If statment) ===========================================
num = 7
if num > 0:
    print("Positive number")
elif num < 0:
     print("Negative number")
else:
    print("Zero")
#=========================================== Loops ===========================================
# For Loop = used to iterate over a sequence (string,list,tuple,set)
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for i in range(10):
    print(i)

for i in range(1,20,2): # => 1,2,4,6,8,.... +2
    print(i)

name = "Yazan Ali"
for latter in name :
    print(latter , end="_") # => Y_a_z_a_n_ _A_l_i

for i in range(10,0,-1):
    print(i) # => 10,9,8,7,6,.... -1
    time.sleep(1) # To sleep 1 second
# While Loop # if 1 == 1 : print("...") => if statment only can axcute a one
while 1 == 1:
    print("I am stuck in a loop!")

age = int(input("Enter your age:"))
while age < 0 :
    print("Age can't be less than 0")
    age = int(input("Enter your age:"))

print(f"Your age is {age} years old")
#=========================================== TypeCasting ===========================================
# Its process of converting a variable frome one data type to another
# str() , int() , float(), bool()
name = "Yazan Ali"
age = 25
gpa = 3.2
is_student = True
# Get type of variable
print(type(name)) # => <class 'str'>

# To convert any dataType to another dataType
age_str = str(age) # int to str
print(type(age_str)) # => <class 'str'>
gpa_int = int(gpa) # float to int
print(type(gpa_int)) # => <class 'int'>
is_student_str = str(is_student) # bool to str
print(type(is_student_str)) # => <class 'str'>
age_float = float(age) # int to float
print(type(age_float)) # => <class 'float'>

name = bool(name) # => The output is be True becouse the string is not empty
print(type(name)) # => <class 'bool'>
empty_str = "" # => empty string
print(bool(empty_str)) # => The output is be False becouse the string is empty
zero = 0
print(bool(zero)) # => The output is be False becouse the number is zero

 #=========================================== Input in python ===========================================
# input() function to get user input
user_name = input("Enter your name: ")
print(f"Hello, {user_name}!")
user_age = input("Enter your age: ")
print(f"You are {user_age} years old.")
user_age = int(user_age) # Convert age to integer
next_year_age = user_age + 1
print(f"Next year, you will be {next_year_age} years old.")
# Note: input() function always returns a string, so we need to convert it to int or float if needed.
#=========================================== List[],Tuple(),set{} ===========================================
# List [] => mutable , most flexible
# Tuple() => immutable , faster
# Set{} => mutable (add/remove), unordered, no duplicates , best for membership testing

fruit = ["apple","banana","orange","coconut"]
print(fruit)
print(fruit[0]) # => If you need to print value through index

fruit[1] = "mango" # => to change the vlaue through index 
fruit.append("grass") # => Add a value to the list
fruit.remove("mango") # => remove the value
fruit.clear() # remove all values in the list

for f in fruit :
    print(fruit,end="-")

# If you need to make list immutable and faster you can replace 
# [] to () to become a Tuple
fruit = ("apple","banana","orange","coconut") # => We can't change the elements

# If you need to make list unordered and no duplicated you can replace 
# [] to {} to become a Tuple
fruit = {"apple","banana","orange","coconut"} # => We can add a new elements
fruit.add("mango")
fruit.remove("coconut")
if "apple" in fruit:
    print("Apple was found")
else :
    print("pineapple was not found")

#=========================================== List of lists ===========================================
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# House information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom",bed],
         ["bathroom",bath]]

# Print out house
print(house)

#=========================================== Subset and conquer ===========================================
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[2])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[0:6])

#=========================================== Slicing and dicing ===========================================
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[0:6]

# Use slicing to create upstairs
upstairs = areas[6:]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)

#=========================================== Subsetting lists of lists ===========================================
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Subset the house list
house[-1][1]

#=========================================== Replace list elements ===========================================
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4] = "chill zone"

#=========================================== Extend a list ===========================================
# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas+["poolhouse",24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1+["garage",15.45]

#=========================================== Delete list elements ===========================================
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Delete the poolhouse items from the list
del areas[10]
del areas[10]

# Print the updated list
print(areas)

#=========================================== Familiar functions ===========================================
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)

#=========================================== pow() function ===========================================
#📌 ما هي pow()؟
# pow() هي دالة مدمجة (built-in function) في بايثون تُستخدم لحساب الأسس (power).
# like this => pow(base, exp, mod=None)
# base → الرقم الأساسي (العدد الذي سترفعه للأس).
# exp → الأس (إلى أي قوة تريد أن ترفع العدد).
# mod → (اختياري) عدد لتطبيق modulus بعد العملية.

print(pow(10, 2))        # 100
print(pow(3, 4, 5))     # (3**4) % 5 = 81 % 5 = 1
print(pow(10, -2))   # 0.01  (لأنه 1 / (10**2))
print(pow(38, -1, 97))   # 23   (modular inverse)

#=========================================== Multiple arguments ===========================================
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True)

# Print out full_sorted
print(full_sorted)

#=========================================== String Methods ===========================================
# string to experiment with: place
place = "poolhouse"

# Use upper() on place
place_up = place.upper()

# Print out place and place_up
print(place)
print(place_up)

# Print out the number of o's in place
print(place.count('o'))

#=========================================== List Methods ===========================================
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))

#=========================================== List Methods (2) ===========================================
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)
