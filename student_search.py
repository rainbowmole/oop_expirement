from student import StudentInfo

class SearchStud:
    def __init__(self, file = "allstudents.txt"):
        self.file = file

    def searchstud(self, Idnum):
        with open(self.file, "r") as file:
            for line in file:
                student = StudentInfo.from_line(line)
                if student.getIdnum() == Idnum:
                    print("\n\t Student Found!")
                    print("\t Student's Info")
                    print(student)
                    return 
            
        print("Student not found...")
    
    def printAllStudentInfo(self):
        with open(self.file, "r") as file:
            students = [StudentInfo.from_line(line) for line in file]
            if students:
                print("\n======== All Student's Information ========\n")
                for student in students:
                    print(student)
            else:
                print("No student found.")