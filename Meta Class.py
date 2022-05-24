class Meta(type):
    def __init__(cls, name, bases, attrs):
        cls.max_coord = 100
        cls.min_coord = 0

class Point(metaclass=Meta):
    def get_coords(self):
        return 0, 0

pt = Point()
print(pt.max_coord)