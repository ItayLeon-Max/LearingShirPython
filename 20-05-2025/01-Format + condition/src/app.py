# Format 
# syntax for Format: print(f"Hello {variable}")

x = 3
y = 5
z = 5

print(x > 5)
print(x < 5)
print(x <= 5)

num = int(input("Enter a number: ")) #6423
left_digit = num // 1000 
second_left_digit = (num // 100) % 10
right_digit = num % 10
second_right_digit = (num // 10) % 10

result = ((left_digit + second_left_digit) == ((right_digit + second_right_digit)*2))
print(f"Result: {result}")

# and / or / not -
# ----------------
# and - both conditions must be true
# or - at least one condition must be true
# not - negates the condition

# condition
# Syntax: if (condition):
x = 5
if (x>5):
    print("x is greater than 5")

if((x<5) and (x>0)):
    print("x is less than 5 and bigger than 0")    

if((x<5) or (x>0)):
    print("x is less than 5 or bigger than 0")    

if(not(x<5)):
    print("x is not less than 5")

if(((x<5) and (x>0))) or (x==5):
    print("x is less than 5 and bigger than 0 or x is equal to 5")  

if((((x<5) and (x>0)) or ((x==5)) and (x<10))):
    print("x is less than 5 and bigger than 0 or x is equal to 5 and x is less than 10")
