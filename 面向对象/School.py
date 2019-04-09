#！/usr/bin/python3
# -*- coding：UTF-8 -*-

class SchoolMember:
    '''代表任何学校里的成员'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        '''我的基本信息'''
        print('Name:"{}" Age:"{}"'.format(self.name, self.age))

class Teacher(SchoolMember):
    '''代表一个老师'''

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher:{})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('(Salary: {:d})'.format(self.salary))

class Student(SchoolMember):
    '''代表一个学生'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks:"{:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('liupeng', 25, 75)

print()

members = [t, s]
for member in members:
    # 对于全体师生工作
    member.tell()













