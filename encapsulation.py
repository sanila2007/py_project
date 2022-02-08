class MathsClass:
    x = 15
    __y = 20;

    def method(self):
        return self.__y


myobject = MathsClass()
print(myobject.x)
print(myobject.method)

print("---------------------------------")


class test:
    def method1(self):
        print("This is a test")  # This is a public method
        self.__method2()

    def __method2(self):
        print("This is a private method")  # Private methods


privateobject = test()
privateobject.method1()

print("------------------------------------")


class phone:
    def phone1(self):
        print("Samsung")
        self.__pjone2()

    def __pjone2(self):
        print("Nokia")


phoneobject = phone()
phoneobject.phone1()

print("-----------------------------------")


class country:
    def country1(self):
        print("I'm from Sri lanka")
        self.__country2()

    def __country2(self):
        print("My motherland is sri lanka")


countryobject = country()
countryobject.country1()
