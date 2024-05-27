import math


class Circle:
    name = ''
    radius = 0.0
    diameter = 0.0

    def set_name(self):
        self.name = 'circle'
        return self.name

    def set_diameter(self):
        diameter = float(self.radius) * 2
        return float(diameter)

    def set_radius(self):
        self.radius = input('Enter the radius of the circle: ')
        return float(self.radius)

    def area(self):
        area = math.pi * float(self.radius) * float(self.radius)
        return area

    def perimeter(self):
        perimeter = 2 * math.pi * self.set_diameter()
        return perimeter

    def circumference(self):
        circumference = math.pi * self.set_diameter()
        return circumference

    def display(self):
        print('RADIUS OF THE ' + self.name.upper() + ' = ' + self.radius)
        print('DIAMETER OF THE ' + self.name.upper() + ' = ' + str(self.set_diameter()))
        print('CIRCUMFERENCE OF THE ' + self.name.upper() + ' = ' + str(self.circumference()))
        print('PERIMETER OF THE ' + self.name.upper() + ' = ' + str(self.perimeter()))
        print('AREA OF THE ' + self.name.upper() + ' = ' + str(self.area()))


circle = Circle()
circle.set_name()
circle.set_radius()
circle.set_diameter()
circle.perimeter()
circle.circumference()
circle.area()
circle.display()
