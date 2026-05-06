class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id, course, marks):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 85:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "Fail"

    def display_student(self):
        self.display_info()
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.calculate_grade()}")


class GraduateStudent(Student):
    def __init__(self, name, age, student_id, course, marks, research_topic):
        super().__init__(name, age, student_id, course, marks)
        self.research_topic = research_topic

    def display_research(self):
        self.display_student()
        print(f"Research Topic: {self.research_topic}")