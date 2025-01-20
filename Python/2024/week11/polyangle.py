from math import tan, pi, cos
from sys import argv


class Polyangle:
    # TODO: init method with variables
    def __init__(self, n, length) -> None:
        self.n = n
        self.length = length
        self.__polygons = {
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

    # TODO: calculate and return exterior angle
    def exterior(self):
        return 360 / self.n

    # TODO: calculate and return interior angle
    def interior(self):
        return 180 - self.exterior()

    # TODO: calculate and return perimeter
    def perimeter(self):
        return self.n * self.length

    # TODO: calculate and return inradius
    def inradius(self):
        # need some math here to calculate inradius or apothem
        return tan(self.interior() * pi / 360) * self.length / 2

    # TODO: calculate and return circumradius
    def circumradius(self):
        # need some math here to calculate circimradius
        return self.inradius() / cos(pi / self.n)

    # TODO: calculate and return area
    def area(self):
        return self.inradius() * self.perimeter() / 2

    # TODO: return the name of the polygon
    def name(self):
        return self.__polygons.get(self.n, f"{self.n}-sided polygon")

    # TODO: return the representation string
    def __repr__(self):
        n = self.n
        ln = self.length
        i = self.interior()
        e = self.exterior()
        p = self.perimeter()
        a = self.area()
        ir = self.inradius()
        cr = self.circumradius()
        nm = self.name()
        return (
            f"Name: {nm}\nSides: {n}\nSide Length: {ln}\n"
            f"Interior angle: {i:.2f}°\nExterior angle: {e:.2f}°\nPerimeter: {p:,.2f}\n"
            f"Area: {a:,.2f}\nInradius: {ir:,.2f}\nCircumradius: {cr:,.2f}"
        )


if __name__ == "__main__":
    # for testing
    print(Polyangle(int(argv[1]), float(argv[2])))
