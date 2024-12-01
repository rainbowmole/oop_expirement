from student import StudentInfo

class openACc:
    def __init__(self, file = "allstudents.txt"):
        self.file = file

    def open_studentAcc(self, idnum):
        with open(self.file, "r") as file:
            for line in file:
                student = StudentInfo.from_line(line)
                if student.getIdnum() == idnum:
                    print(f"\nWelcome, {student.getName()}!")
                    return student
        print("ID not found...")
        return False
    