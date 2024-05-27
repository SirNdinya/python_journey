class Shape2D:
    name = ''
    length = 0
    width = 0

    @classmethod
    def set_length(cls):
        cls.length = input('Enter length')
        return cls.length

    @classmethod
    def set_width(cls):
        cls.width = input('Enter width')
        return cls.width

    @classmethod
    def perimeter(cls):
        perimeter = 2 * (cls.length + cls.width)
        return perimeter

    @classmethod
    def area(cls):
        area = cls.length * cls.width
        return area


rec = Shape2D()
rec.set_width()
rec.set_length()
rec.perimeter()
rec.area()
