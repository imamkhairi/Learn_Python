# classes and object

# from the Student file import Student class
from Student import Student

# from import itu untuk import spesifik member dari sebuah module
# import itu untuk import semua member dari sebuah module

student1 = Student("Jake", "Business", 3.1, False)
student2 = Student("Pam", "Art", 2.5, True)

print(student1.gpa)
print(student2.gpa)