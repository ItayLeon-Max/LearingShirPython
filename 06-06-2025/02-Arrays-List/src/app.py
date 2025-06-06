#Arrays/Lists
#Syntax: Array_name = [item1, item2, item3]

#Example

arr1 = [1, 2, 3, 4, 5, 10]
number = 10
arr2 = [True, False, True, False]
arr3 = ["Hello", "World", "Python"]
arr4 = [1, "Hello", True, 3.14]
objectArr = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
    True,
    42
]

name = "Shir" #['S', 'h', 'i', 'r']
print(name[1])

#Print Arrays:
#Option 1
#Syntax: print(Array_name)
print(arr1)

#Option 2
#Syntax: print(Array_name[index])
print(arr2[0])

#Option 3
#Syntax: for index in Array_name: print(index)
for i in arr4:
    print(i)

#Option 4    
#Syntax: for index in range(len(Array_name)): print(Array_name[index])
for i in range(len(arr3)):
    print(arr3[i])

#Print even numbers from arr1  ---->  [1, 2, 3, 4, 5] 
for i in range(len(arr1)):
    if(arr1[i] % 2 == 0):
        print(arr1[i]) 

#with ternary operator
for i in range(len(arr1)):
    print(arr1[i]) if arr1[i] % 2 == 0 else None

# print from arr3: ["Hello"] ----> ['e'] from "Hello"
for i in range(len(arr3)):
    if arr3[i] == "Hello":
        print(arr3[i][1])

if number in arr1:
    print("Number is in the array")
else:
    print("Number is not in the array")


list1 = list()    
list1.append(1)
for i in list1:
    print(i)

print(len(objectArr))


my_array = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

print(type(my_array))
print(type(my_tuple))


arr5 = [1,2,3,4,5,5,6,7,8,9,10]
print(arr5[:])
print(arr5[:-1])
print(arr5[::-1])