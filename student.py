import os

class StudentInfo:
    def __init__(self, allstudents = "allstudents.txt"):
        self.allstudents = allstudents
    
    def setName(self, name):
        self.name = name
    
    def setAge(self, age):
        self.age = age
    
    def setIdnum(self, idnum):
        self.idnum = idnum
    
    def setEmail(self, email):
        self.email = email
    
    def setPhone(self, phone):
        self.phone = phone
    
    def getName(self):
        return self.name

    def getAge(self):
        return self.age
    
    def getIdnum(self):
        return self.idnum
    
    def getEmail(self):
        return self.email

    def getPhone(self):
        return self.phone
    
    @classmethod
    def from_line(cls, line):
        parts = line.strip().split(",")
        
        if len(parts) != 5:
            print(f"Skipping invalid line: {line.strip()}")
            return None  
    
        name, age, idnum, email, phone = [part.strip() for part in parts]

        student = cls()
        student.setName(name)
        student.setAge(int(age))
        student.setIdnum(idnum)
        student.setEmail(email)
        student.setPhone(phone)
        return student
    
    def to_line(self):
        return f"{self.name},{self.age},{self.idnum},{self.email},{self.phone}"

    def save(self):
        with open(self.allstudents, "a") as file:
            file.write(self.to_line() + "/n")
    
    def __str__(self):
        return f"\nName: {self.name}\n Age: {self.age}\n Id number: {self.idnum}\n Email: {self.email}\n Phone number: {self.phone}"
    
    