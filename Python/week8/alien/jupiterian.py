from alien import Alien


class Jupiterian(Alien):
    def __init__(self, wings, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wings = wings

    def __str__(self) -> str:
        return f"{type(self).__name__}: {super().__str__()}, {self.wings} wings"


if __name__ == "__main__":
    martian = Jupiterian(eyes=7, legs=9, height=3.6, wings=3)
    print(martian)
