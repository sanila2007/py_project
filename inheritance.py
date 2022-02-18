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

print("-----------------------------")


class parent:
    def functionn1(self):
        print("Hello world")


class child(parent):
    def functionn2(self):
        print("Hello!")


parent_object = child()
parent_object.functionn1()
parent_object.functionn2()

print("----------------------------")


class big_table_brand:
    def brand(self):
        print("Damro")


class small_table_brand(big_table_brand):
    def brand2(self):
        super().brand()
        print("Arpico")


table_object = small_table_brand()
table_object.brand2()

print("-----------------------------")


class mouse:
    def brand(self):
        print("Mimeide")


class mouse2(mouse):
    def brand2(self):
        super().brand()
        print("Dell")


mouse_object = mouse2()
mouse_object.brand2()

print("------------------------------------")


class fruits:
    no_of_items = None
    unit_price = None

    def set_value(self, x, y):
        self.no_of_items = x
        self.unit_price = y


class apple(fruits):
    def price(self):
        print("Apple Price =", self.no_of_items * self.unit_price)


class orange(fruits):
    def price(self):
        print("Orange Price =", self.no_of_items * self.unit_price)


class banana(fruits):
    def price(self):
        print("Banana Price =", self.no_of_items * self.unit_price)


apple_object = apple()
orange_object = orange()
banana_object = banana()


apple_object.set_value(10, 15)
orange_object.set_value(40, 100)
banana_object.set_value(1000, 50)

apple_object.price()
orange_object.price()
banana_object.price()

