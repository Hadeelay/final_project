
"""ITF 07 Final Project Attendance System
# TODO 1 Enter your name and submission date
Name :Hadeel Daher
Delivery Date :25/6/2023
"""


# TODO 2 Define Course Class and define constructor with
    def __init__(self, name, mark):
        self.course_id = uuid.uuid4()
        self.name = name
        self.mark = mark

class Student:
    # TODO 3 define static variable indicates total student count
    class Student:
    total_student = 0
    def __init__(self, name):
        self.name = name
        Student.total_student += 1

    def __init__(self, name, age, number):
        self.student_id = uuid.uuid4()
        self.name = name
        self.age = age
        self.number = number
        self.courses = []
    def __init__(self):
        pass

     def enroll_course(self, course):
            self.courses.append(course)
    # TODO 5 define a method to enroll new course to student courses list

    # method to get_student_details as dict
     def get_student_info(self):
            return self.__dict__

    # method to get_student_courses
    
    def get_student_courses(self):
            for course in self.courses:
                print(f"{course.name}: {course.mark}")):

# TODO 6 print student courses with their marks
        pass

    # method to get_student_average 
    def get_student_average(self):
            total_marks = 0
            for course in self.courses:
                total_marks += course.mark
            return total_marks / len(self.courses)
        # TODO 7 return the student average
        pass


# in Global Scope
# TODO 8 declare empty students list

while True:

    while True:
    try:
        selection = int(input("1.Add New Student\n"
                              "2.Delete Student\n"
                              "3.Display Student\n"
                              "4.Get Student Average\n"
                              "5.Add Course to student with mark.\n"
                              "6.Exit"))
    except ValueError:
        print("Invalid input, please enter a number between 1 and 6.")
        continue

    if selection == 1:

        # TODO 10 make sure that Student number is not exists before
        student_number = input("Enter Student Number")
        Is_existing_student = False
        for student in students:
            if student.number == student_number:
                is_existing_student = True
                break

        if is_existing_student:
            print("Student with this number exists.")
        else:
            student_name = input("Enter Student Name")
            while True:
                try:
                    student_age = int(input("Enter Student Age"))
                    break
                except:
                    print("Invalid Value")


        # TODO 11 create student object and append it to students list

        student_courses = []
            students.append(student)

            print("Student Added Successfully")


    elif selection == 2:
        student_number = input("Enter Student Number")
        # TODO 12 find the target student using loops and delete it if exist , if not print ("Student Not Exist")

    elif selection == 3:
        student_number = input("Enter Student Number")
        # TODO 13 find the target student using loops and print student detials  if exist , if not print ("Student Not Exist")

    elif selection == 4:
        student_number = input("Enter Student Number")
        # TODO 14 find the target student using loops and get student average  if exist , if not print ("Student Not Exist")

    elif selection == 5:
        student_number = input("Enter Student Number")
        # TODO 15 ask user to enter course name and course mark then create coures object then append it to target student courses

    else:
        # TODO 16 call a function to exit the program
        pass
final_project.py
جارٍ عرض final_project.py.
