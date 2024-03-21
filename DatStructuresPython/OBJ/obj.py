class Student:

    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    # This is to print something if we only print the object
    def __str__(self):
        return 'This is a Student Class'

    def display(self):
        print(f'Student Name: {self.name}')
        print(f'Roll Number: {self.roll}')
        print(f'Marks:{self.marks}')

    def display2(self):
        print('Student Name:', self.name)
        print('Roll Number:', self.roll)
        print('Marks:', self.marks)


S = Student('aaa', 101, 78.25)
S2 = Student('bbb', 102, 62.55)
S.display()
print('\n\n')
S2.display()
