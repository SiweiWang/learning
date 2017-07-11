students = []


class Student:
    school_name = "awesome high"

    def __init__(self, name, student_id=332):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return 'Student ' + self.get_name_capitalized() + " with id " + str(self.student_id) + " from school " + \
               self.get_school_name()

    def get_name_capitalized(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name


class HighSchoolStudent(Student):
    school_name = "Springfield High"

    def get_school_name(self):
        return "this is a high school student"

    def get_name_capitalized(self):
        original_value = super().get_name_capitalized()
        return original_value + "-HS"



