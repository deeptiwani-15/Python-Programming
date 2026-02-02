# Input marks for 3 subjects
marks = tuple(map(int, input("Enter marks for 3 subjects (space-separated): ").split()))

if len(marks) != 3:
    print("Please enter exactly 3 marks.")
else:
    # Find highest and lowest marks
    highest = max(marks)
    lowest = min(marks)

    # Calculate average
    average = sum(marks) / len(marks)

    # Display results
    print("Marks:", marks)
    print("Highest mark:", highest)
    print("Lowest mark:", lowest)
    print("Average mark:", average)