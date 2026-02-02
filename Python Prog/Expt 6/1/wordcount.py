file_name = "course_outcomes.txt"

try:
    with open(file_name, "r") as file:
        content = file.read()

    # Split the content into words using whitespace
    words = content.split()
    word_count = len(words)

    print(f"The file '{file_name}' contains {word_count} words.")

except FileNotFoundError:
    print(f"The file '{file_name}' does not exist.")