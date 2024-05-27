import datetime
from typing import override

class Shapes:
    name = ''
    date_of_creation = ''
    length: float = 0.0
    width: float = 0.0


    @classmethod
    def set_name(cls):
        cls.name = input('Enter the name of the shape:')
        return cls.name

    @classmethod
    def set_date_of_creation(cls):
        cls.date_of_creation =  datetime()
        return cls.date_of_creation

    @ classmethod
    def set_length(cls):
        cls.length = float(input('Enter length'))
        return cls.length

    @ classmethod
    def set_width(cls):
        cls.width = float(input('Enter width'))
        return cls.width

    @ classmethod
    def find_perimeter(cls):
        return 2*(cls.length + cls.width)

    @ classmethod
    def find_area(cls):
        return cls.length * cls.width

    def display(self):
        print('NAME = ' + self.set_name())
        print('CREATED ON ' + str(self.set_date_of_creation()))
        print('LENGTH = ' + str(self.set_length()))
        print('WIDTH = ' + str(self.set_width()))
        print('PERIMETER OF ' + self.name.upper() + ' = ' + str(self.find_perimeter()))
        print('AREA OF ' + self.name.upper() + ' = ' + str(self.find_area()))

class Circle(Shapes):
    radius: float = 0.0
    PI = 3.14

    @classmethod
    def set_radius(cls):
        cls.radius = float(input('Enter the radius'))
        return cls.radius

    @classmethod
    def find_diameter(cls):
        return 2 * cls.set_radius()

    @ classmethod
    def find_circumference(cls):
        return Circle.PI * cls.find_diameter()

    @ classmethod
    @override
    def find_area(cls):
        return Circle.PI * pow(cls.radius, 2)

    @ classmethod
    @override
    def find_perimeter(cls):
        return (Circle.PI * cls.find_diameter() )+ cls.find_perimeter()

    @override
    def display(self):
        print('NAME = ' + self.set_name())
        print('CREATED ON ' + str(self.set_date_of_creation()))
        print('RADIUS = ' + str(self.set_length()))
        print('DIAMETER = ' + str(self.set_width()))
        print('CIRCUMFERENCE OF ' + self.name.upper() + ' = ' + str(self.find_circumference()))
        print('PERIMETER OF ' + self.name.upper() + ' = ' + str(self.find_perimeter()))
        print('AREA OF ' + self.name.upper() + ' = ' + str(self.find_area()))


class Triangle(Shapes):
    height: float = 0.0
    base: float =0.0

    @classmethod
    def set_base(cls):
        cls.base = float(input('Enter the base: '))
        return  cls.base

    @classmethod
    def set_height(cls):
        cls.height = float(input('Enter the height: '))
        return cls.height

    @ classmethod
    def find_hypotenous(cls):
        m1 = pow(Triangle.base,2)
        m2 = pow(Triangle.height, 2)
        hypotenous = pow((m1 + m2), .5)
        return hypotenous

    @ classmethod
    @ override
    def find_perimeter(cls):
        return Triangle.find_hypotenous()+ Triangle.height + Triangle.width

    @ classmethod
    @override
    def find_area(cls):
        return 0.5 * (Triangle.height * Triangle.base)

    @override
    def display(self):
        print('NAME = ' + self.set_name())
        print('CREATED ON ' + str(self.set_date_of_creation()))
        print('BASE = ' + str(self.base))
        print('HEIGHT = ' + str(self.height))
        print('HYPOTENOUS ' + self.find_hypotenous())
        print('PERIMETER OF ' + self.name.upper() + ' = ' + str(self.find_perimeter()))
        print('AREA OF ' + self.name.upper() + ' = ' + str(self.find_area()))




rectangle = Shapes()
rectangle.set_name()
rectangle.set_date_of_creation()
rectangle.set_width()
rectangle.set_length()
rectangle.set_name()
rectangle.display()

print("==================================================================================")
print("==================================================================================")

c = Circle()
c.set_name()
c.set_date_of_creation()
c.set_radius()
c.find_diameter()
c.find_circumference()
c.find_perimeter()
c.find_area()
c.display()

print("==================================================================================")
print("==================================================================================")
t = Triangle()
t.set_name()
t.set_date_of_creation()
t.set_base()
t.set_height()
t.find_hypotenous()
t.find_area()
t.find_perimeter()
t.display()












