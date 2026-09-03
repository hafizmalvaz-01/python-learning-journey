class person:
    def __init__(self, name, age ):
        self.name = name
        self.age = age

class teacher(person):
    def __init__(self,name, age, subject, role, information):
        super().__init__( name, age)
        self.subject = subject
        self.role = role
        self.information = information

    def teacher_info(self):
        print("Hi! Your name is ", self.name, "\n Your Subject is ", self.subject, "\n Your is to be ", self.role, "\n", self.information)

class student(person):
    def __init__(self, marks, name, age):
        super().__init__( name, age)
        self.marks = marks

    def showinfo(self):
        print(self.name)
        print(self.marks)
        print(self.age)

    def is_passed(self, total):
        
        if self.marks > (total/2):
            return True
        else:
            return False

    def pass_fail(self, passed):
        if passed == True:
            print("COnGraTulaTion!!!! You are Passed")
        else:
            print("COnGraTulaTion!!!! You are Fail")

# main

student1 = student(489,"Alvaz", 22)
student1.showinfo()

passed_1 = student1.is_passed(505)

student1.pass_fail(passed_1)

teacher1 = teacher("SIr", 26, "Chemistry", "Head Teacher","Hard working with unbeatable posession.")
teacher1.teacher_info()