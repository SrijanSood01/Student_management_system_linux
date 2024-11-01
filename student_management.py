import json
import os

# Define the path for the student data file
data_file = 'students.json'

# Function to load student data from the JSON file
def load_data():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    return []

# Function to save student data to the JSON file
def save_data(students):
    with open(data_file, 'w') as file:
        json.dump(students, file, indent=4)

# Function to add a new student
def add_student(students):
    name = input("Enter student's name: ")
    roll_number = input("Enter roll number: ")
    course = input("Enter course: ")
    students.append({'name': name, 'roll_number': roll_number, 'course': course})
    save_data(students)
    print("Student added successfully!")

# Function to view all students
def view_students(students):
    if not students:
        print("No students found.")
        return
    print("\nStudent List:")
    for student in students:
        print(f"Name: {student['name']}, Roll Number: {student['roll_number']}, Course: {student['course']}")

# Function to update student details
def update_student(students):
    roll_number = input("Enter the roll number of the student to update: ")
    for student in students:
        if student['roll_number'] == roll_number:
            student['name'] = input("Enter new name: ")
            student['course'] = input("Enter new course: ")
            save_data(students)
            print("Student details updated successfully!")
            return
    print("Student not found.")

# Function to delete a student record
def delete_student(students):
    roll_number = input("Enter the roll number of the student to delete: ")
    for student in students:
        if student['roll_number'] == roll_number:
            students.remove(student)
            save_data(students)
            print("Student deleted successfully!")
            return
    print("Student not found.")

# Main function to run the menu
def main():
    students = load_data()
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_students(students)
        elif choice == '3':
            update_student(students)
        elif choice == '4':
            delete_student(students)
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == '__main__':
    main()
