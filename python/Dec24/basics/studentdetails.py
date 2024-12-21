"""
student details.py

This module contains the necessary functions to store 
student details
"""

from dataclasses import dataclass, asdict
import json
import os


@dataclass
class Student:
    """This class represents student"""

    name: str
    email: str
    course: str


# This is memory of our application
student_dict = dict()

DATASTORE_PATH = "studentdetails.json"


def add_student():
    """
    This function adds the student info
    """

    name = input("Enter student's name: ")
    course = input("Enter Course: ")
    email = input("Enter email id: ")
    student = Student(name=name, email=email, course=course)
    student_dict[email] = asdict(student)
    with open(DATASTORE_PATH, mode="w", encoding="utf-8") as student_file:
        json.dump(student_dict, student_file, indent=4)


def fetch_student_details():
    """
    This function fetches the student details
    """
    email = input("Enter the email id of the student: ")
    if email in student_dict:
        student = Student(**student_dict[email])
        print(f"name = {student.name}")
        print(f"email = {student.email}")
        print(f"course = {student.course}")
    else:
        print("student not found...")


def initialize_data():
    """This method will read all the data from
    json file into student dictionary if the file exists
    """
    if os.path.exists(DATASTORE_PATH):
        with open(DATASTORE_PATH, mode='r', encoding="utf-8") as students_file:
            global student_dict 
            student_dict = json.load(students_file)

def menu():
    """
    This is menu for the application
    """
    initialize_data()
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
