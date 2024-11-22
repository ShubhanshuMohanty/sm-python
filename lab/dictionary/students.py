# Dictionary of students and their grades
students = {
    "Arjun": "A",
    "Rohan": "B",
    "Kartik": "C"
}

# Print all students and grades
print("Students:", students)

# Print a specific student's grade
print("Grade of Arjun:", students["Arjun"])

# Print a specific student's grade using get method
print("Grade of Kartik:", students.get("Kartik"))

# Print all student names
print("Student Names:", students.keys())

# Update a student's grade
students.update({"Kartik": "A"})
print("Updated Students:", students)

# Add a new student
students.update({"Vikram": "C"})  
print("Added Vikram:", students)

# Add another student
students["Samar"] = "B"
print("Added Samar:", students)

# Remove the last added student
print("Removing item:", students.popitem())
print("After removal:", students)

# Loop through all student names
for student_name in students:
    print("Student Name:", student_name)
for student_name in students.keys():
    print("Student Name:", student_name)

# Loop through all grades
for grade in students.values():
    print("Grade:", grade)

# Loop through all students and grades
for student_name, grade in students.items():
    print("Student Name:", student_name, "Grade:", grade)

# Remove a specific student
removed_student = students.pop("Vikram", None)  
if removed_student is not None:
    print("Removed Student Vikram:", removed_student)
else:
    print("Student Vikram not found.")

# Print final list of students
print("Final Students:", students)
