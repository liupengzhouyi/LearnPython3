Python从设计之初就已经是一门面向对象的语言，正因为如此，在Python中创建一个类和对象是很容易的。本章节我们将详细介绍Python的面向对象编程。

如果你以前没有接触过面向对象的编程语言，那你可能需要先了解一些面向对象语言的一些基本特征，在头脑里头形成一个基本的面向对象的概念，这样有助于你更容易的学习Python的面向对象编程。

接下来我们先来简单的了解下面向对象的一些基本特征。

## 创建类

    class Student:
        '这是一个学生类'
        studentCount = 0
    
        def __init__(self, name, sex, age, number):
            self.name = name
            self.sex = sex
            self.age = age
            self.number = number
            Student.studentCount = Student.studentCount + 1
    
    
    
        def printeeee(self):
            print('-------------------------')
            print('| student name: ', self.name)
            print('| student number: ', self.number)
            if (self.sex == 0):
                print('| student sex: 男')
            else:
                print('| student sex: 女')
            print('| student age:', self.age)
            print('-------------------------')



## 使用类

    from 面向对象.Employee import Student
    
    print(Student.__doc__)
    
    
    t = Student("liupeng", 0, 21, "16671259125")
    t.printeeee()
    
    print(Student.studentCount)
    
    
## 对当前类的解释


    
    
    

    
    
    
    