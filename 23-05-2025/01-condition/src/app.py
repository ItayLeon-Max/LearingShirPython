# Condition
number = 10
if (number > 0):
    print("Positive number")

#Syntax 2: if (condition):(code) else:(code)   
# Example 1
number = -10
if (number > 0):
    print("Positive number")
else:
    print("Negative number")    


#syntax 3: if (condition):(code) elif (condition):(code) else:(code)
# elif: else if   
# Example 2
number = 0
if (number > 0):
    if (number > 10):
        print("Greater than 10")
    elif (number < 10):
        print("Less than 10")
    else:
        print("Equal to 10")        
elif (number == 0):
    print("Zero")
else:
    print("Negative number")
    
#ex1
char = input("Enter a character: ")
if((char >= 'A' and char <= 'Z') or (char >= 'a' and char <= 'z')):
    print("character")
elif (char >= '0' and char <= '9'):
    print("digit")
else:
    print("special character")    

#ex2
# score = int(input("Enter your score: "))
# message = ""
# if(score >= 90 and score <= 100):
#     message = "Excellent"
# elif((score >= 80) and (score < 90)):
#     message = "Very Good"
# elif((score >= 60) and (score < 80)):
#     message = "Passed"
#     if((score >= 60) and (score < 70)):
#         print("You should work hard")
# else:
#     print("Failed")

grade = int(input("Enter your grade: "))
message = ""
if((grade >=90) and (grade <= 100)):
    message = "Excellent"
else:
    if((grade >= 80) and (grade < 90)):
        message = "Very Good"
    else:
        if((grade >= 60) and (grade < 80)):
            message = "Passed"
            if((grade >= 60) and (grade < 70)):
                message = "You should work hard"
        else:
            message = "Failed"
print(message)
             