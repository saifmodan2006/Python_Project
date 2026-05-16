# Define the story template with placeholders in curly braces {}
story_template = """
Today I went to the {adjective} {place}.
I saw a {noun} trying to {verb}.
It was the most {adjective} day ever!
"""

# Welcome message
print("Welcome to the Python Mad Libs Generator!")
print("Please provide the following words:")

# Collect user input for each placeholder
adjective1 = input("Enter an adjective: ")
place = input("Enter a place: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective2 = input("Enter another adjective: ")

# Generate the final story using the collected inputs
# The .format() method can also be used, e.g., story_template.format(...)
final_story = f"""
Today I went to the {adjective1} {place}.
I saw a {noun} trying to {verb}.
It was the most {adjective2} day ever!
"""

# Print the completed story
print("\nYour Mad Libs Story:")
print("-" * 30)
print(final_story)
print("-" * 30)
