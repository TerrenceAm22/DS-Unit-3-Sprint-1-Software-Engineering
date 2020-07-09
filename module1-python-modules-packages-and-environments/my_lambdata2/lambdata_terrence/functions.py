import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from pandas import DataFrame

class Helper_Functions:
    def add_columns(self):
        """ When activated it will add a column 
        into existing dataframe
        """
        df = pd.DataFrame({10, 20, 40, 60, 70, 80, 80, 100, 110, 120})
        names = pd.DataFrame({'Mario', 'Sonic', 'Sly', 'Duke', 'Tails', 'Luigi', 'CaptainMak', 'Crash', 'Knuckles', 'Tupac'})
        result = df.append(names, sort=False)
        return df
    def train_validate_test(self):
        """ Function will split data into
        train and test sets for machine learning
        """
        df = pd.DataFrame({10, 20, 40, 60, 70, 80, 80, 100, 110})
        train_test_split(df, test_size=.5)
        return df.shape
h = Helper_Functions()
print(h.train_validate_test())
print(h.add_columns())

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0 - 100
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()


            return value / len(self.students)


s1 = Student("Tim", 19, 95)
s2 = Student("Ashli", 22, 98)
s3 = Student("Ava", 22, 80)

course = Course("Math", 2)
course.add_student(s1)
course.add_student(s3)
print(course.students[1].name)
print(course.get_average_grade())
