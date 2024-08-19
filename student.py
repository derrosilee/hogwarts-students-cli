import csv
import os

from tabulate import tabulate


class Student:
    def __init__(
        self, first_name, last_name, admission_number, guardian_name, house, sex, grade
    ):
        if not first_name:
            raise ValueError("First name cannot be empty.")
        self.first_name = first_name
        self.last_name = last_name
        self.admission_number = admission_number
        self.guardian_name = guardian_name
        self.house = house
        self.sex = sex
        self.grade = grade

    @classmethod
    def add_student(cls):
        first_name = input("Enter your first name: ").capitalize()
        last_name = input("Enter your last name: ").capitalize()
        admission_number = get_int("Enter your admission number: ")
        guardian_name = input("Enter your guardian name: ").capitalize()
        house = get_house("Enter your house: ").capitalize()
        sex = input("Enter Gender: ").capitalize()
        grade = get_int("Enter your grade: ")

        # check if the file exists if not create it
        file_exists = os.path.isfile("students.csv")
        is_empty = os.stat("students.csv").st_size == 0 if file_exists else True
        with open("students.csv", "a", newline="") as file:
            field_names = [
                "first_name",
                "last_name",
                "admission_number",
                "guardian_name",
                "house",
                "sex",
                "grade",
            ]
            writer = csv.DictWriter(file, fieldnames=field_names)
            if is_empty:
                writer.writeheader()
            writer.writerow(
                {
                    "first_name": first_name,
                    "last_name": last_name,
                    "admission_number": admission_number,
                    "guardian_name": guardian_name,
                    "house": house,
                    "sex": sex,
                    "grade": grade,
                }
            )
        print(f"Student added successfully: {first_name} {last_name}")
        return cls(
            first_name, last_name, admission_number, guardian_name, house, sex, grade
        )

    @classmethod
    def view_students(cls):
        with open("students.csv", "r") as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            print(tabulate(data, headers="keys", tablefmt="fancy_grid"))

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.admission_number} {self.guardian_name} {self.house} {self.sex} {self.grade}"


# to check if user has inputted an integer if false re prompt the user
def get_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Please enter an integer.")
        return get_int(prompt)


# to check if user has inputted a valid house if false re prompt the user
def get_house(prompt):
    houses = ["Gryffindor", "Slitherin", "RavenClaw"]
    try:
        house = input(prompt).capitalize()
        if house not in houses:
            raise ValueError("House must be one of the following: " + ", ".join(houses))
        return house
    except ValueError:
        print("Please enter a valid house.")
        return get_house(prompt)
