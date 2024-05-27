class Square:
    name = ''
    length: int = 0
    width: int = 0

    @classmethod
    def set_name(cls):
        cls.name = 'Square'
        return cls.name

    @classmethod
    def set_length(cls):
        cls.length = int(input('Enter the length: '))
        return cls.length

    @classmethod
    def set_width(cls):
        cls.width = int(input('Enter the width: '))
        return cls.width

    @classmethod
    def perimeter(cls):
        perimeter = int(2 * (cls.length + cls.width))

        return perimeter

    @classmethod
    def area(cls):
        area = int(cls.length * cls.width)
        return area

    def display(self):
        print('NAME = ' + self.name)
        print('LENGTH = ' + str(self.length))
        print('WIDTH = ' + str(self.width))
        print('PERIMETER OF ' + self.name.upper() + ' = ' + str(self.perimeter()))
        print('AREA OF ' + self.name.upper() + ' = ' + str(self.area()))


print('lets find area and perimeter of a square!!!!!!!!!!')

square = Square()

square.set_name()
square.set_length()
square.set_width()
square.perimeter()
square.area()
square.display()
