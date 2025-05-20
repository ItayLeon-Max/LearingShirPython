# Format 
# syntax for Format: print(f"Hello {variable}")

x = 3
y = 5
z = 5

print(x > 5)
print(x < 5)
print(x <= 5)

num = int(input("Enter a number: ")) #6323
left_digit = num // 1000 
second_left_digit = (num // 100) % 10
right_digit = num % 10
second_right_digit = (num // 10) % 10

result = ((left_digit + second_left_digit) == ((right_digit + second_right_digit)*2))
print(f"Result: {result}")