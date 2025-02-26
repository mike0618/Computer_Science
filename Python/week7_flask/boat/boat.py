from motor import Motor
from passenger import Passengers


class Boat:
    def __init__(self) -> None:
        self.__motor = Motor()
        self.__passengers = Passengers()

    def sail(self):
        self.__motor.start()

    def dock(self):
        self.__motor.stop()

    def main(self):
        for _ in range(5):
            self.__passengers.onboard()
        print(f"{self.__passengers.get_num()} passengers boarded.")
        self.sail()
        print(self.__motor)
        print("Boat is sailing.")
        self.dock()
        print(self.__motor)
        print("Boat is docking.")
        self.__passengers.disembark()
        print("1 passenger disembarked.")
        print(f"{self.__passengers.get_num()} passengers are on the boat.")


if __name__ == "__main__":
    boat = Boat()
    boat.main()
