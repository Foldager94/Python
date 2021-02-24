[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Foldager94/Python/HEAD)
# python Handin Christoffer Foldager

Week 1 assignments done



class Course:

    def __init__(self, name, classroom, teacher, etcs, grade=-1):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.etcs = etcs
        self.grade = grade
        
        
import Course
class DataSheet:

    def __init__(self, courses=[]):
        self.courses = courses

    def grades_as_list(self):
        lst = []
        for x in self.courses:
            lst.append(x.grade)
        return lst


    def __str__(self):
        String = ""
        for c in self.courses:
            String += "," + c.name + "," + c.teacher + "," + str(c.classroom) + "," + str(c.etcs) + "," + str(c.grade)
        return ","+str(len(self.courses)) + String +"\n"
        
        
        
        
import DataSheet

class Student:
    def __init__(self, name, gender, image_url, data_sheet):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    def get_avg_grade(self):
        grades = self.data_sheet.grades_as_list()
        sum_of_grades = 0
        for grade in grades:
            sum_of_grades += int(grade)
        avg_grade = int(sum_of_grades)/len(grades)
        return avg_grade

    def progression_in_percent(self):
        total_sum = 150
        sum = 0
        for course in self.data_sheet.courses:
            sum += int(course.etcs)

        sum_in_procent = (sum/total_sum)*100
        return sum_in_procent

    def __str__(self):
        return self.name + "," + self.gender + "," + self.image_url + self.data_sheet.__str__()




import Student
import random
import DataSheet
import Course
import csv
import matplotlib.pyplot as plt

def generate_student(n, out="output.txt"):
    StudentNameList = ["Andreas", "Alex", "Benjamin", "Nicolas", "Christoffer", "Lars", "Kim", "Henrik", "Victor", "Lenny", "Kasper", "Bo", "Hans"]
    TeatcherName = ["Lise", "kurt", "Arne", "Tess", "Nicolaj"]
    ClassRoom = [1,2,3,4,5,6,7,8,9]
    CourseName = ["Math", "Chemestry", "Gym", "Danglish", "English", "Computer Science", "physics"]
    Grades = [-3, 00, 2, 4, 7, 10, 12]
    ECTS = 25
    Students = []
    with open(out, 'w') as o:
        for x in range(n):
            course1 = Course.Course(random.choice(CourseName), random.choice(ClassRoom), random.choice(TeatcherName), random.randrange(10, 50, 5), random.choice(Grades))
            course2 = Course.Course(random.choice(CourseName), random.choice(ClassRoom), random.choice(TeatcherName), random.randrange(10, 50, 5), random.choice(Grades))
            course3 = Course.Course(random.choice(CourseName), random.choice(ClassRoom), random.choice(TeatcherName), random.randrange(10, 50, 5), random.choice(Grades))
            data = DataSheet.DataSheet([course1, course2, course3])
            newStudent = Student.Student(random.choice(StudentNameList), "Male", "Image_url", data)
            Students.append(newStudent)
            o.write(newStudent.__str__())
    return Students

def retrive_students_from_csv(input):
    student_list = []
    with open(input, 'r') as o:
        reader = csv.reader(o)
        for row in reader:
            number_of_courses = int(row[3])
            courses_list = []
            number = 0
            x=0
            while x < number_of_courses:
                courses_list.append(Course.Course(row[4+number], row[5+number], row[6+number], row[7+number], row[8+number]))
                number += 5
                x += 1
            student_list.append(Student.Student(row[0], row[1], row[2], DataSheet.DataSheet(courses_list)))
    return student_list


def print_name_avg(list):
    for student in list:
        avg_grade = student.get_avg_grade()
        name = student.name
        img = student.image_url
        print("Navn:", name, " image:", img, " average grade:", avg_grade)

def sort_by_avg_grade(list):
    sorted_list = sorted(list, key=lambda obj: obj.get_avg_grade(), reverse=True)
    return sorted_list

def var_plot(list):
    name = []
    avg_grade = []
    for student in list:
        name.append(student.name)
        avg_grade.append(student.get_avg_grade())
    plt.bar(name, avg_grade, width=0.5, align='center')
    plt.xticks(rotation=45, horizontalalignment='right', fontweight='light')
    plt.show()

def etcs_plot(list):
    procent = [10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0]
    number_of_students = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    student_etcs= []
    for student in list:
        student_etcs.append(student.progression_in_percent())

    for etcs in student_etcs:
        etcs_index_0 = str(etcs)[0]
        index = switch_case_etcs(etcs_index_0)
        number_of_students[index] = number_of_students[index] + 1


    plt.bar(procent, number_of_students, width=0.5, align='center')
    #plt.xticks(rotation=45, horizontalalignment='right', fontweight='light')
    plt.show()

def switch_case_etcs(n):
    return {
        '1' : 0,
        '2' : 1,
        '3' : 2,
        '4' : 3,
        '5' : 4,
        '6' : 5,
        '7' : 6,
        '8' : 7,
        '9' : 8,
        '10' : 9
    }[n]

