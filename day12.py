#string slicing and fucntions of strings 
fruit = "Mango"
len1 = len(fruit)  #len counts the number of alphabets in strings and returns it
print("Mango is a", len1, "letter word.")

#string as an array

pie = "ApplePie"
print(pie[:5])
print(pie[6])	#returns character at specified index

#slicing example

pie = "ApplePie"
print(pie[:5])      #Slicing from Start
print(pie[5:])      #Slicing till End
print(pie[2:6])     #Slicing in between
print(pie[-8:])     #Slicing using negative index