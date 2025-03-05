class Alien:
    def __init__(self, eyes: int, legs: int, height: float) -> None:
        self.eyes: int = eyes
        self.legs: int = legs
        self.height: float = height

    def __str__(self) -> str:
        return f"Alien height is {self.height} feet.\n\tIt has {self.legs} legs, {self.eyes} eyes"
