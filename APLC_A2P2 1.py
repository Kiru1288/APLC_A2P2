
import datetime
import nt
import time
from datetime import date, datetime
from time import localtime
import sys
from xmlrpc.client import boolean


class APLC_A2P2:
    # this is the student object for when we add/remove/update/view a student's profile

    f_name = None
    l_name = None
    dob = None
    sex = "x"
    pre_gpa = 0.0
    cur_semester = 0
    program = None
    course_count = 0

    def __init__(self, f_name, l_name, dob, sex, pre_gpa,
                 cur_semester, program, course_count):

        self.f_name = f_name
        self.l_name = l_name
        self.dob = dob
        self.sex = sex
        self.pre_gpa = pre_gpa
        self.cur_semester = cur_semester
        self.program = program
        self.course_count = course_count

    # in python theres no need to use getters and setters as opposed to java,
    # we can use the existing APLC_A2P2 object to access the attributes directly


student_list = []


def createStudentList():

    # dob is in yyyy/mm/dd

    student_list.append(APLC_A2P2("Benjamin", "Simms", date(2005, 12, 20), "m", 3.75, 1, "Software Development", 5))

    student_list.append(APLC_A2P2("Wasim", "Borhot", date(2005, 12, 20), "m", 3.75, 1, "Software Development", 5))

    student_list.append(APLC_A2P2("Michael", "Fortier", date(2004, 9, 20), "m", 3.6, 1, "Software Development", 5))

    student_list.append(APLC_A2P2("Kiru", "Hankebo", date(2005, 12, 20), "m", 3.75, 1, "Software Development", 5))

    student_list.append(APLC_A2P2("Andrew", "Dung Le", date(2005, 12, 20), "m", 3.75, 1, "Software Development", 5))

    student_list.append(APLC_A2P2("Eunice", "Olugbemiro", date(2007, 1, 31), "f", 3.9, 1, "Natural Science", 4))

    student_list.append(APLC_A2P2("Michael", "Myers", date(1957, 10, 19), "m", 3.05, 3, "Culinary Arts", 3))

    student_list.append(APLC_A2P2("Jason", "Voorhees", date(1946, 6, 13), "m", 0, 0, "Kinesiology", 6))

    student_list.append(APLC_A2P2("Freddy", "Kruger", date(1942, 5, 13), "m", 1.36, 13, "Sleep Medicine", 4))

    student_list.append(APLC_A2P2("Ghost", "Face", date(1978, 4, 7), "m", 3.75, 1, "Psychology", 4))


user_f_name = None
user_l_name = None


def adminView():

    # This will be for accessing the student list

    print("=" * 30)
    print("WELCOME TO ADMIN VIEW: " + str(user_l_name))
    print("=" * 30)

    print(
        "SELECT ADMIN OPTION\n"
        "1: view specific student\n"
        "2: view all students\n"
        "3: add student\n"
        "4: remove student\n"
        "5: edit student\n"
        "9:log out"
    )

    print("=" * 30)

    user_input = input("Enter number: ")

    match user_input:

        case "1":
            searchStudent(user_input)

        case "4":
            searchStudent(user_input)

        case "2":
            viewAllStudents()

        case "3":
            addStudent()

        case "5":
            editStudent()

        case "9":
            print("[!] Logging out, goodbye!")
            sys.exit(0)

        case _:
            print("\n[!] Invalid option, try again!\n")
            adminView()


def getUserInput():
    return input()


# This one will be used to find and remove students
def searchStudent(user_input):

    print("Enter student first name:")
    selected_f_name = getUserInput().upper()

    print("Enter student last name:")
    selected_lname = getUserInput().upper()

    found_student = False
    student_id = 0

    # no students ? no list

    if len(student_list) == 0:
        print("[!] No students in the list, please add a student first!")
        adminView()

    else:
        # find the student first
        # always display the student no matter the option
        # gotta get all their info before removing to make sure we have the right student

        print("=" * 30)

        for i in range(len(student_list)):

            if (student_list[i].f_name.upper() == selected_f_name
                    and student_list[i].l_name.upper() == selected_lname):

                found_student = True
                student_id = i

                print("Student found: " + student_list[i].f_name + " " + student_list[i].l_name)
                print("DOB: " + str(student_list[i].dob))
                print("Sex: " + student_list[i].sex)
                print("Previous GPA: " + str(student_list[i].pre_gpa))
                print("Current Semester: " + str(student_list[i].cur_semester))
                print("Program: " + student_list[i].program)
                print("Course Count: " + str(student_list[i].course_count))

        # if it cant find the student, then error

        if not found_student:
            print("Error: Student " + selected_f_name + " " + selected_lname + " not found in the list!")
            adminView()

        else:

            # for finding a student

            if user_input == "1":
                print("=" * 30)
                print("> Search for another student? (y/n): ")
                next_option = getUserInput()

                if next_option.upper() == "Y":
                    found_student = False
                    searchStudent(user_input)

                elif next_option.upper() == "N":
                    found_student = False
                    adminView()

                else:
                    found_student = False
                    print("ERR: Invalid input! Returning to Admin View.")
                    adminView()

            # for deleting a student

            elif user_input == "4":
                print("> Remove this student? (y/n): ")
                next_option = getUserInput()

                if next_option.upper() == "Y":
                    found_student = False
                    student_list.pop(student_id)

                    print("\n[!] Student removed! Returning to Admin View.\n")
                    adminView()

                elif next_option.upper() == "N":
                    found_student = False
                    adminView()

                else:
                    found_student = False
                    print("ERR: Invalid input! Returning to Admin View.")
                    adminView()


def viewAllStudents():

    if (student_list is None) or (len(student_list) == 0):
        print("[!] No students in the list, please add a student first!")
        adminView()

    else:
        print("=" * 30)

        for i in range(len(student_list)):
            print("Student " + str(i + 1) + ": " + student_list[i].f_name + " " + student_list[i].l_name)

            print("=" * 30)

        print("all students shown, returning to Admin View")
        adminView()


def editStudent():

    print("Enter student first name:")
    selected_f_name = getUserInput().upper()

    print("Enter student last name:")
    selected_lname = getUserInput().upper()

    found_student = False
    student_id = 0

    # no students ? no list

    if len(student_list) == 0:
        print("[!] No students in the list, please add a student first!")
        adminView()

    else:
        # find the student first

        print("=" * 30)

        for i in range(len(student_list)):

            if (student_list[i].f_name.upper() == selected_f_name
                    and student_list[i].l_name.upper() == selected_lname):

                found_student = True
                student_id = i

                print("Student found: " + student_list[i].f_name + " " + student_list[i].l_name)
                print("DOB: " + str(student_list[i].dob))
                print("Sex: " + student_list[i].sex)
                print("Previous GPA: " + str(student_list[i].pre_gpa))
                print("Current Semester: " + str(student_list[i].cur_semester))
                print("Program: " + student_list[i].program)
                print("Course Count: " + str(student_list[i].course_count))

        # if it cant find the student, then error

        if not found_student:
            print("Error: Student " + selected_f_name + " " + selected_lname + " not found in the list!")
            adminView()

        else:

            print("=" * 30)

            print(
                "SELECT ATTRIBUTE TO EDIT\n"
                "1: First Name\n"
                "2: Last Name\n"
                "3: Date of Birth\n"
                "4: Sex\n"
                "5: Previous GPA\n"
                "6: Current Semester\n"
                "7: Program\n"
                "8: Course Count\n"
                "9: Return to Admin View"
            )

            print("=" * 30)

            user_input = getUserInput()

            match user_input:

                case "1":
                    print("Enter new first name:")
                    new_f_name = getUserInput()
                    student_list[student_id].f_name = new_f_name[0:1].upper() + new_f_name[1:]

                case "2":
                    print("Enter new last name:")
                    new_l_name = getUserInput()
                    student_list[student_id].l_name = new_l_name[0:1].upper() + new_l_name[1:]

                case "3":
                    try:
                        print("Enter new birth year (yyyy):")
                        new_dob_year = getUserInput()

                        print("Enter new birth month (mm):")
                        new_dob_month = getUserInput()

                        print("Enter new birth day (dd):")
                        new_dob_day = getUserInput()

                        student_list[student_id].dob = date(
                            int(new_dob_year),
                            int(new_dob_month),
                            int(new_dob_day)
                        )

                    except ValueError:
                        print("ERR: Invalid date of birth. Student information unchanged.")

                case "4":
                    print("Enter new student sex:")
                    new_sex = getUserInput()

                    if len(new_sex) > 0:
                        student_list[student_id].sex = new_sex[0].lower()
                    else:
                        print("ERR: Invalid input. Student information unchanged.")

                case "5":
                    try:
                        print("Enter new previous GPA:")
                        new_prev_gpa = float(getUserInput())

                        if 0 <= new_prev_gpa <= 4.0:
                            student_list[student_id].pre_gpa = new_prev_gpa
                        else:
                            print("ERR: GPA must be between 0 and 4.0.")

                    except ValueError:
                        print("ERR: Invalid GPA. Student information unchanged.")

                case "6":
                    try:
                        print("Enter new current semester:")
                        new_cur_semester = int(getUserInput())

                        student_list[student_id].cur_semester = new_cur_semester

                    except ValueError:
                        print("ERR: Invalid semester. Student information unchanged.")

                case "7":
                    print("Enter new program:")
                    new_program = getUserInput()

                    if len(new_program) > 0:
                        student_list[student_id].program = new_program[0:1].upper() + new_program[1:]
                    else:
                        print("ERR: Invalid program. Student information unchanged.")

                case "8":
                    try:
                        print("Enter new course count:")
                        new_course_count = int(getUserInput())

                        student_list[student_id].course_count = new_course_count

                    except ValueError:
                        print("ERR: Invalid course count. Student information unchanged.")

                case "9":
                    adminView()

                case _:
                    print("ERR: Invalid option!")
                    adminView()

            # display updated student information

            print("=" * 30)
            print("UPDATED STUDENT INFORMATION")

            print("Student: " + student_list[student_id].f_name + " " + student_list[student_id].l_name)
            print("DOB: " + str(student_list[student_id].dob))
            print("Sex: " + student_list[student_id].sex)
            print("Previous GPA: " + str(student_list[student_id].pre_gpa))
            print("Current Semester: " + str(student_list[student_id].cur_semester))
            print("Program: " + student_list[student_id].program)
            print("Course Count: " + str(student_list[student_id].course_count))

            print("=" * 30)
            print("[!] Student updated! Returning to Admin View.")
            adminView()


def addStudent():

    # naming
    print("Enter new student first name: ")
    new_f_name = getUserInput()
    new_f_name = new_f_name[0:1].upper() + new_f_name[1:]

    print("Enter new student last name: ")
    new_l_name = getUserInput()
    new_l_name = new_l_name[0:1].upper() + new_l_name[1:]

    new_dob = None

    # facts
    print("Enter new student birth year (yyyy): ")
    new_dob_year = getUserInput()

    print("Enter new student birth month (mm): ")
    new_dob_month = getUserInput()

    print("Enter new student birth day (dd): ")
    new_dob_day = getUserInput()

    try:
        new_dob = date(int(new_dob_year), int(new_dob_month), int(new_dob_day))

    except ValueError:
        print("ERR: Invalid date of birth. Returning to Admin View.")
        adminView()

    print("New student date of birth is: " + new_dob_year + "-" + new_dob_month + "-" + new_dob_day)

    print("Enter new student sex: ")
    new_sex = getUserInput()

    # school
    print("Enter new student previous GPA: ")
    new_prev_gpa = getUserInput()

    print("Enter new student current semester: ")
    new_cur_semester = getUserInput()
    new_cur_semester = new_cur_semester[0:1].upper() + new_cur_semester[1:]

    print("Enter new student program: ")
    new_program = getUserInput()
    new_program = new_program[0:1].upper() + new_program[1:]

    print("Enter new student course count: ")
    new_course_count = getUserInput()

    new_student = APLC_A2P2(
        new_f_name,
        new_l_name,
        new_dob,
        new_sex[0],
        float(new_prev_gpa),
        int(new_cur_semester),
        new_program,
        int(new_course_count)
    )

    print("\nSTUDENT: " + new_student.l_name + ", " + new_student.f_name)
    print("DOB: " + str(new_student.dob))
    print("SEX: " + new_student.sex)
    print("PREV GPA: " + str(new_student.pre_gpa))
    print("SEMESTER: " + str(new_student.cur_semester))
    print("PROGRAM: " + new_student.program)
    print("COURSE COUNT: " + str(new_student.course_count))

    student_list.append(new_student)

    print("\n[!] New student added! Returning to Admin View.\n")
    adminView()


def loginSequence():
    return False


def logoutSequence():
    return False


createStudentList()
adminView()
