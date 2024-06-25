# Dictionary of student marks in five subjects
student_marks = {
    'student1': [55, 65, 75, 85, 95],
    'student2': [45, 55, 65, 75, 85],
    'student3': [60, 70, 80, 90, 100],
    'student4': [35, 45, 55, 65, 75],
    'student5': [50, 60, 70, 80, 90]
}

# Calculate average marks for each student
average_marks = {}
for student, marks in student_marks.items():
    average_marks[student] = sum(marks) / len(marks)

# Find the student with the maximum and minimum average marks
max_avg_student = max(average_marks, key=average_marks.get)
min_avg_student = min(average_marks, key=average_marks.get)

print(f"Student with the highest average marks: {max_avg_student} with an average of {average_marks[max_avg_student]}")
print(f"Student with the lowest average marks: {min_avg_student} with an average of {average_marks[min_avg_student]}")
