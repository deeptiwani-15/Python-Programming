try:
    # Take user input for age
    age = int(input("Enter your age: "))

except ValueError:
    # Handle invalid (non-integer) input
    print("Invalid input! Please enter a valid integer for age.")

else:
    # This block executes if no exception occurs
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote. You must be at least 18 years old.")

finally:
    # This block always executes
    print("Thank you for using the voting eligibility checker.")