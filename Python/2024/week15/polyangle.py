from math import tan, pi, cos


class Polyangle:
    # TODO: init method with variables
    def __init__(self) -> None:
        self.__n: int
        self.__length: float

    # TODO: Sides setter
    def sides(self, n):
        self.__n = n

    # TODO: Length setter
    def side_len(self, length):
        self.__length = length

    # TODO: calculate and return exterior angle
    def exterior(self):
        return 360 / self.__n

    # TODO: calculate and return interior angle
    def interior(self):
        return 180 - self.exterior()

    # TODO: calculate and return perimeter
    def perimeter(self):
        return self.__n * self.__length

    # TODO: calculate and return inradius
    def inradius(self):
        # need some math here to calculate inradius or apothem
        return tan(self.interior() * pi / 360) * self.__length / 2

    # TODO: calculate and return circumradius
    def circumradius(self):
        # need some math here to calculate circimradius
        return self.inradius() / cos(pi / self.__n)

    # TODO: calculate and return area
    def area(self):
        return self.inradius() * self.perimeter() / 2

    # TODO: return the name of the polygon
    def name(self):
        polygons = {
            3: "Triangle",
            4: "Quadrilateral",
            5: "Pentagon",
            6: "Hexagon",
            7: "Heptagon",
            8: "Octagon",
            9: "Nonagon",
            10: "Decagon",
            11: "Hendecagon",
            12: "Dodecagon",
            13: "Tridecagon",
            14: "Tetradecagon",
            15: "Pentadecagon",
            16: "Hexadecagon",
            17: "Heptadecagon",
            18: "Octadecagon",
            19: "Enneadecagon",
            20: "Icosagon",
        }
        return polygons.get(self.__n, f"{self.__n}-sided")
