from student_module import Student, GraduateStudent

print("----- Student Info -----")
s1 = Student("Ali", 20, "S101", "CS", 85)
s1.display_student()

print("\n")

print("----- Graduate Student Info -----")
g1 = GraduateStudent("Hamza", 29, "cs201", "DS", 28, "open source")
g1.display_research()

def print_hi(name):
    print(f'Hi, {name}')  
if __name__ == '__main__':
    print_hi('PyCharm')
