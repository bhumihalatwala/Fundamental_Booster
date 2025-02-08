print("Welcome to the Interactive Personal Data Collector!",end = "\n\n")

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in metres: "))
fav = int(input("Please enter your favorite number: "))

print(end = "\n")

print("Thank you! Here is the information we collected: ", end = "\n\n")

print("Name:",name,"(Type:",type(name),"Memory Address:",id(name),")")
print("Age:",age,"(Type:",type(age),"Memory Address:",id(age),")")
print("Height:",height,"(Type:",type(height),"Memory Address:",id(height),")")
print("Favorite Number:",fav,"(Type:",type(fav),"Memory Address:",id(fav),")")

print(end = "\n")

print("Your birth year is approximately:",2025-age,"(based on your age of ", age,")", end = "\n\n")

print("Thank you for using the Personal Data Collector. Goodbye!")
