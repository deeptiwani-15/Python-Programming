a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Swapping using a temporary variable
temp = a
a = b
b = temp

print("After swapping:")
print("a =", a)
print("b =", b)