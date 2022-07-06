# Types
# string_example = "Hello World!"
# int_example = 12
# float_example = 3.14
# list_example = ["hi", 12, 3.14]
# dict_example = {"name": "Ben", "age": 34}
# tuple_example = (250, "Test")
# bool_example = True
# range_example = range(5)

# Check type
# print(type(string_example))
# print(type(int_example))
# print(type(float_example))
# print(type(list_example))
# print(type(dict_example))

# Strings
# print("hello" == "hello")
# print("hello".upper())  # HELLO
# print("hello".lower())  # hello
# print("hello".capitalize())  # Hello
# string_concat = "hello" + "world"
# string_interpolation = f"expr: {2 + 4}"
# string_len = len(string_interpolation)
# print(string_len)

# Numeric
# sum = 1 + 2
# mult = 2 * 4
# str(sum)
# round(12.41)  # 12
# round(12.41, 1)  # 12.4

# # Lists
# empty_list = []
# beatles = ["john", "ringo", "seb"]
# beatles[0]  # john
# beatles[-1]  # seb
# beatles[2] = "paul"
# print(beatles[1] == beatles[-2])  # True
# beatles.append("george")
# beatles.remove("george")
# print(beatles)
# del beatles[0]
# print(len(beatles))  # 2
# beatles.append("george")
# beatles.append("john")
# print(beatles)  # ['ringo', 'paul', 'george', 'john']
# sorted(beatles)  # ['george', 'john', 'paul', 'ringo']
# # sorted() does not modify original
# beatles.sort()
# # sort() modifies original
# print(beatles)  # ['george', 'john', 'paul', 'ringo']

# # For loop
# for num in range(5):
#     print(num)  # 0 to 4

# for num in range(2, 4):
#     print(num)  # 2 to 3

# for i in range(2, 10, 3):
#     print(i)  # 2, 5, 8

# staff = ["Ben", "Alex", "Arthur", "Sam", "Blair"]
# for member in staff:
#     print(member)

# for index, member in enumerate(staff):
#     print(index, member, sep=": ")
#     print(f"{index}: {member}")

# # List comprehension
# letters = ["a", "b", "c", "d", "e", "f"]
# uppercase_letters = [letter.upper() for letter in letters]
# half_uppercase_letters = [
#     letter.upper() for index, letter in enumerate(letters) if index % 2 == 0
# ]
# print(half_uppercase_letters)

# Dictionaries
# Collection of unique keys with a value associated

# students = {
#     "Peter": 24,
#     "Mary": 25,
#     "George": 22,
# }
# empty_dict = {}
# london = {"country": "England", "population": 8982000}

# print(london["country"])

# london["star_monument"] = "Big Ben"
# london["population"] += 1

# print(london)

# for key in london:
#     print(key, london[key], sep=": ")

# for value in london.values():
#     print(value)

# for key, value in london.items():
#     print(key, value, sep=": ")

# print(len(london))
# # Returns the default value if not exists
# london.get("star_monument", "No monument found")

# # Create dict from lists
# names = ["Peter", "Mary", "Emma"]
# ages = [24, 25, 20]

# students_dict = {name: age for name, age in zip(names, ages)}
# print(students_dict)

# OOP
# Object Oriented Programming

# Class is the mold
# Instance is the cake created from the mold

# Files in Python are defined in lower snake case (lower_snake_case)
# Defined in upper camel case (UpperCamelCase)
# class Car:
#     # Method trigger when instantiation
#     def __init__(self, color: str):
#         self.color = color
#         self.engine_started = False

#     def is_engine_started(self):
#         return self.engine_started

#     def start_engine(self):
#         self.engine_started = True
#         self.sound = "Brroooom"

#     def get_color(self):
#         return self.color


# ferrari = Car("Red")
# print(ferrari.color)
# print(ferrari.engine_started)
# print(ferrari.is_engine_started())
# print(ferrari.start_engine())
# print(ferrari.sound)

# Behaviour set of methods

# Inheritance
# class Building:
#     def __init__(self, name: str, width: float, length: float) -> None:
#         self.name = name
#         self.width = width
#         self.length = length

#     def floor_area(self) -> float:
#         return self.width * self.length


# class Castle(Building):
#     def __init__(self, name: str, width: float, length: float) -> None:
#         super().__init__(name, width, length)
#         self.butler = None

#     def has_a_butler(self) -> bool:
#         return self.butler is not None

#     def floor_area(self) -> float:
#         return super().floor_area() + 300

#     @classmethod
#     def categories(cls):
#         return ["medieval", "Norman", "Ancient"]


# class House(Building):
#     @classmethod
#     def price_per_square_meter(cls, city: str) -> int | str:
#         if city == "Paris":
#             return 9000
#         if city == "Brussels":
#             return 3000
#         return f"No data for {city}"


# class Skyscraper(Building):
#     pass


# # House, Castle and Skyscraper inherit the constructor from Building

# versailles = Castle("Versailles", 100, 100)
# print(versailles.floor_area())
# casa = House("Casa", 10, 5)
# print(casa.floor_area())
# print(Castle.categories())
# print(House.price_per_square_meter("Barcelona"))
