from student import StudentInfo
import os

class AddStudent:   
    def __init__(self, file = "allstudents.txt"):
        self.file = file
    
    def add_student(self, name, age, idnum, email, phone):
        student = StudentInfo(self.file)
        student.setName(name)
        student.setAge(age)
        student.setIdnum(idnum)
        student.setEmail(email)
        student.setPhone(phone)
        student.save()

        print(f'\nAdded student {name} to the list')
    
    def new_student(self):
        print("\n===ADD NEW STUDENT===")
        name, age, idnum, email, phone = input("\nEnter Name: "), int(input("Enter Age: ")), input("Enter ID Number: "), input("Enter Email: "), input("Enter Phone Number: ")
        print("\n===NOTHING FOLLOWS===\n")
        
        self.add_student(name, age, idnum, email, phone)


    

