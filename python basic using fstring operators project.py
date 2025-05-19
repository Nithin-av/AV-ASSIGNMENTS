# Get user input
name = input("Please enter your name: ")
age = input("Please enter your age: ")

# Personalized greeting using the + operator
greeting_plus =  "Hello, " + name +  "! You are " + age + " years old."
print(greeting_plus)

# Personalized greeting using f-strings
greeting_fstring = f"Hi, {name}! You are {age} years old."
print(greeting_fstring)