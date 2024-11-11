#!/usr/bin/env python3
# Author ID: rylle Mendoza

class Student:

    # Initialize the Student object with a name, student number, and an empty dictionary for courses
    def __init__(self, name, number):
        self.name = name  # Store the student's name
        self.number = str(number)  # Convert the student number to a string to avoid errors later
        self.courses = {}  # Initialize an empty dictionary to hold course names and grades

    # Method to display the student's name and number
    def displayStudent(self):
        # Return a formatted string with the student's name and number
        return 'Student Name: ' + self.name + '\n' + 'Student Number: ' + self.number

    # Method to add a course and grade to the student's record
    def addGrade(self, course, grade):
        # Add the course as the key and the grade as the value in the courses dictionary
        self.courses[course] = grade

    # Method to calculate and display the student's GPA
    def displayGPA(self):
        # Check if the student has any courses; if not, return a GPA of 0.0
        if len(self.courses) == 0:
            return f'GPA of student {self.name} is 0.0'

        # Sum up all the grades from the courses dictionary
        total_grade = sum(self.courses.values())
        # If all grades are zero, return a GPA of 0.0 to avoid division by zero issues
        if total_grade == 0:
            return f'GPA of student {self.name} is 0.0'
        
        # Calculate GPA by dividing total grades by the number of courses
        gpa = total_grade / len(self.courses)
        # Format the GPA to one decimal place and return the result
        return f'GPA of student {self.name} is {gpa:.1f}'

    # Method to list courses where the student has passed (grade > 0.0)
    def displayCourses(self):
        # Use a list comprehension to create a list of courses with grades above 0.0
        passed_courses = [course for course, grade in self.courses.items() if grade > 0.0]
        return passed_courses  # Return the list of passed courses

# Only run the following code if the script is executed directly
if __name__ == '__main__':
    # Create a student object with a name and student number, then add grades for each class
    student1 = Student('John', '013454900')
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    # Create another student object with a name and student number, then add grades
    student2 = Student('Jessica', 123456)  # Notice we can use an integer for the number
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)  # This course will be ignored in passed courses

    # Display information for the first student
    print(student1.displayStudent())  # Shows name and number
    print(student1.displayGPA())  # Shows calculated GPA
    print(student1.displayCourses())  # Lists passed courses

    # Display information for the second student
    print(student2.displayStudent())  # Shows name and number
    print(student2.displayGPA())  # Shows calculated GPA
    print(student2.displayCourses())  # Lists passed courses
