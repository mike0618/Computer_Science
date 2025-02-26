class Passengers:
    def __init__(self):
        self.__passengers = 0

    def onboard(self):
        self.__passengers += 1

    def disembark(self):
        if self.__passengers:
            self.__passengers -= 1

    def get_num(self):
        return self.__passengers
