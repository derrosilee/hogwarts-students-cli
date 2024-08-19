from student import Student
import argparse

def main():
    parser = argparse.ArgumentParser(description="Student Management System")
    parser.add_argument('--add', help='Add a student', action='store_true')
    parser.add_argument('--view', help='View students', action='store_true')
    args = parser.parse_args()

    # Check option passed on args
    if args.add:
        Student.add_student()
    elif args.view:
        Student.view_students()
    else:
        print("Please provide an option")


if __name__ == '__main__':
    main()
