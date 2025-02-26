class Motor:
    def __init__(self):
        self.__running = False

    def start(self):
        self.__running = True

    def stop(self):
        self.__running = False

    def is_running(self):
        return self.__running

    def __str__(self):
        if self.__running:
            return "Motor is running."
        return "Motor is stopped."
