class Student:

    def __init__(self, name, lastname, department, year_of_entrance):
        self.name = name
        self.lastname = lastname
        self.department = department
        self.year_of_entrance = year_of_entrance


    def get_student_info(self):
        print(f"The student's info is as follows: First name : {self.name} Last name : {self.lastname} entered in {self.year_of_entrance} faculty: {self.department}")

s = Student('Asel', 'Yrysova', 'FEC', 1999)
s.get_student_info()

