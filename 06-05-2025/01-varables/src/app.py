print("Hello, World!") #printing to console
# This is a simple Python script that prints "Hello, World!" to the console.

print("first string", "second string") # printing multiple strings

# variable assignments - strings
name = "Shir Shlomy"
print(name)

print("Hello World!") 
print("Hello \nWorld!") # printing with a new line with \n
print("Hello \"World!\"") # printing with a backslash with \"
print("Hello \tWorld!") # printing with a tab with \t
print("Hello \\World!") # printing with a backslash with \\

# variable assignments
first_name = "Shir"
print("your name is:", first_name)
first_name = "Itay"
print("your name is:", first_name)

last_name = "Leon"
full_name = first_name + " " +  last_name
print("your name is:", full_name)
char1 = "a"
char2 = "b"
sum_chars = char1 + " " + char2
print("sum of chars is:", sum_chars)

#input from user
enter_first_name = input("Enter your first name: ")
print("your name is:", enter_first_name)
enter_age = int(input("Enter your age: ")) # int = integer
print("your age is:", enter_age)

#variable float
float_num = 3.14
enter_float_num = float(input("Enter a float number: "))
print("float number is:", enter_float_num)

#variable boolean
is_name_shir = False
print(type(is_name_shir)) # printing the type of the variable

num_to_string = 5
# str(num_to_string) # converting int to string
print("the number is:" + str(num_to_string)) # printing the type of the variable

age = input("Enter your age: ")
print("your age is:" + age)
next_year =int(age) + 1

number = 5.6
print("the number is:" + str(number))

print(type(number))

PI = 3.14
print(type(PI)) # printing the type of the variable

number_of_tickets = input("Enter the number of tickets: ")
PRICE_PER_TICKET = 40
TOTAL_PRICE = int(number_of_tickets) * PRICE_PER_TICKET # calculating the total price
print("the total price is:" + str(TOTAL_PRICE)) # printing the total price
