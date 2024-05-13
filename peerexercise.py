class person:
    def __init__(self, name, age, CID):
        self.name = name
        self.age = age
        self.CID = CID
    
    def walk(self):
        print(f"{self.name} is waling")

    def talk(self):
        print(f"{self.name} is talking")
    
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class teacher(person):
    def __init__(self, name, age, CID, subject, salary, department, designation):
        super().__init__(name, age, CID)
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation

    def teach(self):
        print(f"{self.name} is teaching")

    def grade_student(self):
        print(f"{self.name} is grading")

    def attend_meeting(self):
        print(f"{self.name} is at meeting")

    
class student(person):
    def __init__(self, name, age, CID,student_id, course, year, GPA):
        super(). __init__(name, age, CID)
        self.student_id = student_id
        self.course = course
        self.year = year
        self.GPA = GPA

    def study(self):
        print(f"{self.name} is studying")

    def attend_class(self):
        print(f"{self.name} is in the class")

    def write_exam(self):
        print(f"{self.name} is wrting exam")


t1 = teacher("karma", 45, 10703003338, "chemistry", 58000, "ECE", "HOD")
std1 = student("pema", 20, 10703003900, 20030102, "ECE", "1st year", 78.83)

t1.teach()
t1.grade_student()
t1.eat()

std1.study()
std1.attend_class()
std1.sleep()




        

