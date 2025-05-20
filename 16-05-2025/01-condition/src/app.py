# Condition & Operator / Logic operators

# syntax: operand1 operator operand2
# operators: +, -, *, /, %, **, // ,==, !=, >, <, >=, <=
num1 = 100
num2 = 2
print(num1 + num2) 
print(num1 ** num2)
# 456 % 10
print(456 % 10)

clock = int(input("Enter the time in 24 hour format (HHMM): "))
print(f"Hour: {clock // 100} \nMinute: {clock % 100}") # this is return the hour and minute

print(1+4+5*3//2%5) 

num = 123.4321
print(f"num = {num:.2f}") 

x = 2
x1 = x - 1 # option 1
x -= 1 # option 2
print(x1, x)
x2 = x + 1 
x += 1 # x++
print(x2, x)