#taking user input in python (17 aug)
# we use input() function to take inputs in python.by default input() fucntion takes anything and treat it as a string

a=input("Enter your name: ")
print("My name is ", a)

x=input("Enter first number: ")
y=input("Enter second number:")
print(x+y)  #here x and y is strings because we dont convert them into int or float
print(int(x) + int(y))
