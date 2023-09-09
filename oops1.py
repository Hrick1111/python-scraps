class Student:
    def __init__(self,name,age,rn):
        self.name=name
        self.age=age
        self.rn=rn

class School:
    def __init__(self):
        self.students=[]
    def add_student(self,name,age,rn):
        student=Student(name,age,rn)
        self.students.append(student)
    def display_students(self):
        for student in self.students:
            print(f"name = {student.name}")
            print(f"age = {student.age}")
            print(f"roll number = {student.rn}")
            print("................................")
    def edit_student(self,rn,new_name,new_age):
        for student in self.students:
            if student.rn==rn:
                student.name=new_name
                student.age=new_age
                print(f"the student name is succesfully upadate to {student.name}")
                return
    def delete_student(self,rn):
        for student in self.students:
            if student.rn==rn:
                self.students.remove(student)
                print(f"the student {student.name} has been deleted succesfully")
                return
        


school=School()
while True:
    choice=input("enter your choice : \n1.Add Student \n2.Display Student details \n3.Edit Roll of Student \n4.Delete roll of student  \n5.Quit")
    if choice=='1':
        name =input("enter the name of the stduent")
        age =input("enter the age of the stduent")
        rn =input("enter the roll of the stduent")
        
        school.add_student(name,age,rn)
    elif choice=='2':
        school.display_students()
    elif choice=='3':
        rn =input("enter the roll you want to edit of the stduent")
        new_name =input("enter the new name of the stduent")
        new_age =input("enter the new age of the stduent")
        school.edit_student(rn,new_name,new_age)
    elif choice=='4':
        rn =input("enter the roll number youo want to delete")
        school.delete_student(rn)
        

    elif choice=='5':
        break



