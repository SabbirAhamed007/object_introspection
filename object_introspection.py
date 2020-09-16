class School:
    no_of_teacher = 200
    no_of_student = 1500
    no_of_classroom = 50

class Teacher:

    def __init__(self, t_fname, t_lname, t_salary, t_subject, t_dob):
        self.t_fname = t_fname
        self.t_lname = t_lname
        self.t_salary = t_salary
        self.t_subject = t_subject
        self.t_dob = t_dob

    def printdetail(self):
        return f"Teacher's name is {self.t_fname} {self.t_lname}. He is good for {self.t_subject} and his salary is {self.t_salary}, dob{self.t_dob}"


class Student:
    def __int__(self, s_fname, s_lname, s_standard, s_gender, s_id, s_dob):
        self.s_fname = s_fname
        self.s_lname = s_lname
        self.s_standard = s_standard
        self.s_gender = s_gender
        self.s_id = s_id
        self.s_dob = s_dob

    def printdetail(self):
        return f"Student name is {self.s_fname} {self.s_lname}. Student id {self.s_id} and standard{self.s_standard}. Gender {self.s_gender} & DOB {self.s_dob}"

class Classroom:

    def __init__(self, c_name):
        self.c_name = c_name

    def printdetail(self):
        return f"Classroom name {self.c_name}"


    @classmethod
    def change_no_teacher(cls, with_substitute_teacher):
        cls.no_of_teacher = with_substitute_teacher

        with_substitute_teacher = int(input("Enter number of substitute teachers"))
        now_no_of_teacher = no_of_teacher + with_substitute_teacher

    def cool_teacher(Teacher, School):
        student_choice = "no_of_star"
        def printstudent_choice(self):
            print(self.student_choice)

Shajhan = Teacher("Shajahan", "Khan", "1800", "Math", "01/02/1980")
Zhang = Teacher("Lu", "Zhang", "1600", "History", "01/02/1983")
Adams = Teacher("Brain", "Adams", "1900", "Song", "01/02/1987")


print(type(Shajhan))

print(type("this is a string"))
print(id("this is a string"))
print(id("this is a string"))
print(id(Zhang))
print(id(Adams))



print(dir(Student))

import inspect
print(inspect.getmembers(Student))


import inspect
print(inspect.getmembers(Teacher))