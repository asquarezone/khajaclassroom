"""
student details.py

This module contains the necessary functions to store 
student details
"""


class Student:
    """This class represents student"""

    def __init__(self, name, course, email):
        self.name = name
        self.email = email
        self.course = course

    def __repr__(self):
        return f"name = {self.name}, email = {self.email}, course = {self.course}"

# This is memory of our application
student_dict = dict()


def add_student():
    """
    This function adds the student info
    """
    name = input("Enter student's name: ")
    course = input("Enter Course: ")
    email = input("Enter email id: ")
    student = Student(name, course, email)
    student_dict[email] = student


def fetch_student_details():
    """
    This function fetches the student details
    """
    email = input("Enter the email id of the student")
    if email in student_dict:
        student = student_dict[email]
        print(f"name = {student.name}")
        print(f"email = {student.email}")
        print(f"course = {student.course}")
    else:
        print("student not found...")


def menu():
    """
    This is menu for the application
    """
    while True:
        choice = input(
            "Enter your choice: 1 for adding students and 2 for student info and 3 for exit: "
        )
        if choice.strip() == "1":
            add_student()
        elif choice.strip() == "2":
            # fetch student
            fetch_student_details()
        else:
            break
    print("Thanks..................")


if __name__ == "__main__":
    menu()
