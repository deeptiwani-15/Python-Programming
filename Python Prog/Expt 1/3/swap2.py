a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Swapping without a temporary variable
a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)
