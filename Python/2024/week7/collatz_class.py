class Collatz:
    """Calculate the Collatz sequence"""

    def get_lst(self, num: int) -> list:
        """Get a list of the Collatz chain:
        Returns:
            list: List of numbers in a the Collatz chain"""
        lst = []
        while num > 1:
            if num % 2:  # if the number is odd
                num = num * 3 + 1
            else:  # it the nujmber is even
                num //= 2
            lst.append(str(num))
        return lst

    # This function gets the length without creating lists
    # I could add conditions to the first one but this way will work quicker
    def get_length(self, num: int) -> int:
        """Get a length of the Collatz chain:
        Returns:
            int: Length of the Collatz chain"""
        lng = 0
        while num > 1:
            if num % 2:  # if the number is odd
                num = num * 3 + 1
            else:  # it the nujmber is even
                num //= 2
            lng += 1
        return lng
