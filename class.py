class Phone:
    def say(self, name):
        self.g = name
        print("Hello" + name)


phone1 = Phone()
phone1.say(" Samsung")
print(phone1.g)
phone1.g = " Nokia"
print(phone1.g)

# We can use self keyword to access to an attributes


phone2 = Phone()
phone2.say(" Apple")

print("_____________________________")


class Friends:
    def guys(self, Names):
        self.nam = Names
        print("These are my friends " + Names)


friend1 = Friends()
friend1.guys("Test 1 friend")
friend1.nam = "Second friend"
print(friend1.nam)

friends2 = Friends()
friends2.guys("Hi i am second guy")

print("------------------------------")


class Student:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


student1 = Student("Amal", "Male")
student2 = Student("Nimal", "Male")

print(student1.name,"'s gender is",student1.gender)
print(student2.name,"'s gender is",student2.gender)

print("--------------------------------------")

a = input("\nWhat's your name? ")
b = input("How old are you? ")

class Details:
    def __init__(self, name, age):
        self.name = name
        self.age = age


studentdetail1 = Details(a, b)
print("Student's name is",a)
print("Student's age is", b)

d = input("What's your name? ")
e = input("How old are you? ")

studentdetail2 = Details(d,e)
print("Student's name is",d)
print("Student's age is", e)

print("-------------------------------")

class test:
    def marks(self, markss):
        self.markss = markss
        print("Sinhala marks", markss)

marks1 = test()
marks1.marks(90)