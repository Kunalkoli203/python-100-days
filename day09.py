# typecasting in python  (14 aug)
#two types of typecasting

# 1.implicit type casting
a=10
b=20.5
c=a+b
print(c)   #automatically converts int to float while adding because of data loss

# 2. explicit type casting(me manually do it without automation)
string="15"
number=7
string_number=int(string) #throws an error if the string is not valid integer. here in this line we use int() method to convert that string into int
sum=number+string_number
print("the sum of both the numbers is:", sum)