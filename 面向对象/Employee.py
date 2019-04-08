#!/usr/bin/python3
# -*- coding: UTF-8 -*-

class Student:
    '这是一个学生类'
    studentCount = 0    # 全局变量

    def __init__(self, name, sex, age, number):
        self.name = name
        self.sex = sex
        self.age = age
        self.number = number
        Student.studentCount = Student.studentCount + 1



    def printeeee(self):
        print('--------------------------------------------------')
        print('| student name: ', self.name)
        print('| student number: ', self.number)
        if (self.sex == 0):
            print('| student sex: 男')
        else:
            print('| student sex: 女')
        print('| student age:', self.age)
        print('--------------------------------------------------')




