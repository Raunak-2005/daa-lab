import random

# List of grades
grades = ['AA', 'AB', 'BB', 'BC', 'CC', 'CD', 'DD', 'FF']

# Function to generate a string of grades
def generate_grade_string():
    return ' '.join(random.choice(grades) for _ in range(40))

# Generate 20 strings of grades
grade_strings = [generate_grade_string() for _ in range(20)]

# Print the results
for idx, grade_string in enumerate(grade_strings, start=1):
    print(f"String {idx}: {grade_string}")
