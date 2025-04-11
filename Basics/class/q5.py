"""April 11, 2025
5. Create a Student Class with a Course
Objective: Define a Student class that stores a student's name and a list of courses.

Requirements:
Initialize the student with name and an empty list of courses.
Add a method add_course(course_name) to add courses to the student's list.
Add a method list_courses() to display all courses the student is taking.

Example Output:
student = Student("Jane")
student.add_course("Math")
student.add_course("Science")
student.list_courses()  # Output: ["Math", "Science"]
"""

class Student:
    def __init__(self,name):
        self.name = name
        self.courses = set()

    
    def add_course(self,course_name):
        self.courses.add(course_name)
    
    def list_courses(self):
        print(self.courses)

student = Student("Jane")
student.add_course("Math")
student.add_course("Science")
student.list_courses()