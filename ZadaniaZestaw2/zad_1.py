class Student:
    name: str
    marks: list

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        marks_avg = sum(self.marks) / len(self.marks)
        marks_tf = True if marks_avg > 50 else False
        return marks_tf

    def __str__(self):
        return f'{self.name} {self.is_passed()}'


student1 = Student('Adam', [20, 30, 40])
print(student1)
