# Take input from the user
string = input("Enter a string: ")

# Remove spaces and convert to lowercase for accurate comparison
cleaned_string = string.replace(" ", "").lower()

# Check if the string is equal to its reverse
if cleaned_string == cleaned_string[::-1]:
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')