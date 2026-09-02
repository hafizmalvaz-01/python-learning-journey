class student:
    def __init__(self, name, marks, age ):
        self.name = name
        self.marks = marks
        self.age = age

    def showinfo(self):
        print(self.name)
        print(self.marks)
        print(self.age)

    def is_passed(self):
        if self.marks > 500/2:
            return True
        else:
            return False

    def pass_fail(self, passed):
        if passed == True:
            print("COnGraTulaTion!!!! You are Passed")
        else:
            print("COnGraTulaTion!!!! You are Fail")

# main

student1 = student("Alvaz", 499, 22)
student2 = student("Usman", 350, 22)
student3 = student("Shery", 489, 22)

student1.showinfo()

passed_1 = student1.is_passed()
passed_2 = student2.is_passed()
passed_3 = student3.is_passed()

student1.pass_fail(passed_1)
student2.showinfo()
student1.pass_fail(passed_2)
student3.showinfo()
student1.pass_fail(passed_3)