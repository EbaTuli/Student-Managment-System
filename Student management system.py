
import sys
import time
def text (t):
    for char in t:
    	sys.stdout.write(char)
    	sys.stdout.flush()
    	time.sleep(0.1)

# Create a dictionary to store student information
students = {
    "1001": {'name': 'Alice', 'score': 85, 'credit_hour': 6, 'test_date': '2023-10-15', 'course': 'Math'},
    "1002": {'name': 'Bob', 'score': 92, 'credit_hour': 6, 'test_date': '2023-10-18', 'course': 'English'}
}

# Function to display menu options
def display_menu():
    text("\n♥ ◆ ♣《《Welcome to Student Management System》♥ ◆ ♣")
    print("\n1. Teacher Login")
    print("2. Student Login")
    print("3. Exit")

# Function for teacher login
# Assume that  only three teachers can use this system and password is given for each of them


teachers = {
    "Eba": "12345",
    "Biniam": "54321",
    "Moibon": "67890"
}
def teacher_login():
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        
        if username in teachers and password == teachers[username]:
            print("Login successful!")
            teacher_menu()
        else:
            print("Invalid username or password. Please try again.")

  

# Function for student login
def student_login():
    student_id = input("\nEnter your ID number: ")

    if student_id in students:
        print("\nLogin successful!")
        student_menu(student_id)
    else:
        print("\nStudent not found. Please contact your teacher.")

# Functions for teacher menu
def teacher_menu():
    while True:
        print("\nTeacher Menu")
        print("1. View Attendance")
        print("2. Mark Attendance")
        print("3. View Student List")
        print("4. Add New Student")
        print("5. Calculate GPA")
        print("6. Logout")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            view_attendance()
        elif choice == 2:
            mark_attendance()
        elif choice == 3:
            view_student_list()
        elif choice == 4:
            add_student()
        elif choice == 5:
            calculate_gpa()
        elif choice == 6:
            print("\nLogged out successfully!")
            break
        else:
            print("\nInvalid choice. Please try again.")

def mark_attendance():
    student_id = input("\nEnter student's ID number: ")

    if student_id in students:
        test1 = input("Enter attendance for Test 1 (Present/Absent): ")
        test2 = input("Enter attendance for Test 2 (Present/Absent): ")
        test3 = input("Enter attendance for Test 3 (Present/Absent): ")

        students[student_id]['attendance'] = {'test1': test1, 'test2': test2, 'test3': test3}
        print("\nAttendance marked successfully!")
    else:
        print("\nStudent not found. Please try again.")

def view_attendance():
    student_id = input("\nEnter student's ID number: ")

    if student_id in students and 'attendance' in students[student_id]:
        attendance = students[student_id]['attendance']
        print("\nAttendance for student", student_id)
        print("Test 1:", attendance['test1'])
        print("Test 2:", attendance['test2'])
        print("Test 3:", attendance['test3'])
    else:
        print("\nAttendance not available or student not found.")
def view_student_list():
    if len(students) > 0:
        print("\nStudent List")
        for student_id, info in students.items():
            print("ID:", student_id)
            print("Name:", info['name'])
            print("Score:", info['score'])
            print("Credit Hour:", info['credit_hour'])
            print("Test Date:", info['test_date'])
            print("Course:", info['course'])
            print()
    else:
        print("\nNo students found.")

def add_student():
    student_id = input("\nEnter student's ID number: ")
    # Check if student already exists
    if student_id in students:
        print("\nStudent already exists. Please try again.")
    else:
        name = input("Enter student's name: ")
        score = float(input("Enter student's score: "))
        credit_hour = int(input("Enter student's credit hour: "))
        test_date = input("Enter student's test date: ")
        course = input("Enter student's course: ")
        students[student_id] = {'name': name, 'score': score, 'credit_hour': credit_hour, 'test_date': test_date, 'course': course}
        print("\nStudent added successfully!")

def calculate_gpa():
    student_id = input("\nEnter student's ID number: ")
    if student_id in students:
        credit_hour = students[student_id]['credit_hour']
        score = students[student_id]['score']
        gpa = score / credit_hour
        print("\nGPA for student", student_id, "is", gpa)
    else:
        print("\nStudent not found. Please try again.")

# Functions for student menu
def student_menu(student_id):
    while True:
        print("\nStudent Menu")
        print("1. View Course")
        print("2. View Result")
        print("3. View Credit Hour")
        print("4. View Test Date")
        print("5. Logout")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            view_course(student_id)
        elif choice == 2:
            view_result(student_id)
        elif choice == 3:
            view_credit_hour(student_id)
        elif choice == 4:
            view_test_date(student_id)
        elif choice == 5:
            print("\nLogged out successfully!")
            break
        else:
            print("\nInvalid choice. Please try again.")

def view_course(student_id):
    if student_id in students:
        print("\nCourse for student", student_id, "is", students[student_id]['course'])
    else:
        print("\nStudent not found. Please try again.")

def view_result(student_id):
    if student_id in students:
        print("\nResult for student", student_id, "is", students[student_id]['score'])
    else:
        print("\nStudent not found. Please try again.")

def view_credit_hour(student_id):
    if student_id in students:
        print("\nCredit Hour for student", student_id, "is", students[student_id]['credit_hour'])
    else:
        print("\nStudent not found. Please try again.")

def view_test_date(student_id):
    if student_id in students:
        print("\nTest Date for student", student_id, "is", students[student_id]['test_date'])
    else:
        print("\nStudent not found. Please try again.")

# Main program
while True:
    display_menu()
    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        teacher_login()
    elif choice == 2:
        student_login()
    elif choice == 3:
        print("\nThank you for using Student Management System!")
        break
    else:
        print("\nInvalid choice. Please try again.")
