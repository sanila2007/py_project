class car1:
    def feature1(self):
        print("Colour")


class car2(car1):
    def feature2(self):
        print("Model")


class car3(car1):
    def feature3(self):
        print("Speed")


carobject = car2()
carobject.feature1()
carobject.feature2()

print("---------------------------")

class laptop:
    def brand(self):
        print("Acre")


class laptop2(laptop):
    def brand2(self):
        print("Dell")

class_object = laptop()
class_object.brand()
