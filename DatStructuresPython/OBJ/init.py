class Student:
    college = 'UCLA'  # This is a static variable

    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks
        Student.college = 'UCLA'  # This is a static variable

    def display(self):
        print('Student Name: ', self.name)
        print('Student Roll No: ', self.roll)
        print('Student Marks: ', self.marks)
        local_variable = "This is a local variable" # This is a local variable
        print('College Name: ', Student.college)
        print(local_variable)


S1 = Student('aaa', 101, 78.25)  # These are instance variables
S2 = Student('bbb', 102, 55.65)
S1.display()
print('\n')
S2.display()
