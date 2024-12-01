import os
from student import StudentInfo
from adds_student import AddStudent
from open_studAcc import openACc
from student_search import SearchStud

student_file = "allstudents.txt"

studAcc = openACc(student_file)
addstud = AddStudent(student_file)
search = SearchStud(student_file)

def main():
    os.system("cls")
    student = None
    for a in range(4):
        b = 3
        idnum = input("\n\nWelcome to student portal!\nEnter student ID number: ")
        student = studAcc.open_studentAcc(idnum)
        if student:
            studportal(student)
        else:
            print(f"Please try again! Number of tries remaining [{b-1}]")
            continue
        
def studportal(student):
    os.system("cls")
    while True:
        print(f"Welcome, {student.getName()}!\n")
        choice = input("Please choose from the following options\n1. View your Information\n2. View other student's information\n3. Register new student\'s info\n4. View all students in the list\n5. Exit\nEnter choice: ")

        if choice == '1': #your info
            search.searchstud(student.getIdnum())
            again = input("\nContinue? [y/n]: ").lower()
            if again == 'y': continue
            else: break
        
        elif choice == '2': #ibang info
            otherid = input("\nEnter the student\'s id number: ")
            search.searchstud(otherid)
            again = input("\nContinue? [y/n]: ").lower()
            if again == 'y': continue
            else: break

        elif choice == '3': #registration
            addstud.new_student()
            again = input("\nContinue? [y/n]: ").lower()
            if again == 'y': continue
            else: break

        elif choice == "4": #view all
            search.printAllStudentInfo()
            again = input("\nContinue? [y/n]: ").lower()
            if again == 'y': continue
            else: break

        elif choice == '5': #exit na
            print("\nThank you for using.")
            break

        else:
            print("Invalid input, please try again."); continue

if __name__ == "__main__":
    main()