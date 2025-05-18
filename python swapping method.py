# Method 1 : Using a third variable
print("Swapping using a third variable:")
var1 = 15
var2 = 30
print(f"Before swapping: var1 = {var1}, var2 = {var2}")

temp  = var1
var1 = var2
var2 = temp
print(f"After swapping: var1 = {var1}, var2 = {var2}")

print("\nSwapping without using a third variable:")
# Method 2: Without using third variable
num1 = 25
num2 = 50
print(f"Before swapping: num1 = {num1}, num2 = {num2}")

num1, num2 = num2, num1

print(f"After swappimg: num1 = {num1}, num2 = {num2}")
