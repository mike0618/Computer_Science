from alien import Alien


class Martian(Alien):
    def __init__(self, arms, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.arms = arms

    def __str__(self) -> str:
        return f"{type(self).__name__}: {super().__str__()}, {self.arms} arms"


if __name__ == "__main__":
    martian = Martian(eyes=3, legs=5, height=7.2, arms=8)
    print(martian)
