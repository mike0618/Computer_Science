print("Tutorial 1: A Car with Class\n")


# Define a "Car" class
class Car:
    # initialize method
    def __init__(self, model, year) -> None:
        # set model and year attrs to the provided parameters
        self.model = model
        self.year = year


# Create an instance of the Car class
my_car = Car("Toyota", 2022)

# print a formatted string using the objects attrs.
print(f"My car is a {my_car.model} from {my_car.year}.")

print("\nTutorial 2: A Person with Class\n")


# define a class Person
class Person:
    # init constructor method
    def __init__(self, name, age) -> None:
        # set attributes
        self.name = name
        self.age = age

    # method to greet and provide information
    def greet(self):
        return f"Hello, my name is {self.name} and I'm {self.age} years old."


# Create and instance (object) of the class
individual = Person("Alice", 25)

# call the greet method
print(individual.greet())

print("\nTutorial 3: Encapsulation by Book\n")


# a blueprint (class) for creating Book objects
class Book:
    def __init__(self, title, author) -> None:
        # set a protected _title attribute, by convention it should not be used outside the class
        self._title = title
        # set a private __author attribute, it cannot not be used outside the class
        self.__author = author

    # get methods for title and author
    def get_title(self):
        return self._title

    def get_author(self):
        return self.__author


# create a book instance
book = Book("To Kill a Mockingbird", "Harper Lee")
# print a formatted string using get methods
print(f"{book.get_title()} by {book.get_author()}")

# Python allows to access protected attributes, but it is not recommended
print(f"\nProtected attribute is possible to access: {book._title}\n")
# but trying to access a private attribute will raise an attribute error
try:
    print(f"Private attribute: {book.__author}")
except AttributeError as e:
    print("Tried to access the private attribute from outside the class.")
    print(e)

print("\nAssignment 1: Online Video Game Store\n")


class Store:
    def __init__(self, title, price) -> None:
        # set a protected _title attribute
        self._title = title
        # set a protected _price attribute
        self._price = price

    def display_game(self):
        return f"{self._title} for ${self._price}"

    # the special method that used by default to print the objects
    def __str__(self) -> str:
        return f"{self._title} for ${self._price}"


games = (
    Store("The Legend of Zelda", 15.99),
    Store("Minecraft", 29.99),
    Store("FIFA 22", 39.99),
)

print("Use the display_game method to print games\n")
for game in games:
    print(game.display_game())

print("\nThe __str__ method works by default for printing\n")
for game in games:
    print(game)
