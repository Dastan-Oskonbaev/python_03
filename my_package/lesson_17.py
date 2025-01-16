# # class Person:
# #     species = "Homo sapiens"
# #
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #
# #
# # person_1 = Person("Timur", 15)
# # person_2 = Person("Nurel", 16)
# #
# # print(person_1.species)
# # print(person_1.name)
# # print(person_1.age)
#
#
# # class Country:
# #     def __init__(self, name, square, population, religion, language="kyrgyz"):
# #         self.name = name
# #         self.square = square
# #         self.population = population
# #         self.religion = religion
# #         self.language = language
# #
# #     def trade(self, country):
# #         print(f"We start trade with {country}")
# #
# #     def stop_trade(self, country):
# #         print(f"We stop trade with {country}")
# #
# # country_1 = Country("Kyrgyzstan", 199000, 7000000,
# #                     "islam")
# #
# # print(country_1.language)
# # country_1.trade("USA")
# # country_1.stop_trade("USA")
#
#
# # class Car:
# #     def __init__(self, mark, model, year, color, price):
# #         self.mark = mark
# #         self.model = model
# #         self.year = year
# #         self.color = color
# #         self.price = price
# #         self.engine_start = False
# #         self.actions = []
# #
# #
# #     def start_engine(self):
# #         if self.engine_start:
# #             return f"{self.model} Engine is already started"
# #         else:
# #             self.engine_start = True
# #             self.actions.append("start engine")
# #             return f"{self.model} Engine is started"
# #
# #     def stop_engine(self):
# #         if not self.engine_start:
# #             return f"{self.model} Engine is already stopped"
# #         else:
# #             self.engine_start = False
# #             self.actions.append("stop engine")
# #             return f"{self.model} Engine is stopped"
# #
# #     def check_engine(self):
# #         if self.engine_start:
# #             return f"{self.model} Engine is works"
# #         else:
# #             return f"{self.model} Engine is not working"
# #
# #     def drive(self):
# #         if self.engine_start:
# #             self.actions.append("driving")
# #             return f"WRUM WRUM"
# #         else:
# #             return "At first start the engine"
# #
# #     def crush(self, amount: int):
# #         self.actions.append("crushing")
# #         self.price = self.price - amount
# #
# #     def repair(self, amount: int):
# #         self.actions.append("repair")
# #         self.price = self.price + amount
# #
# #
# # toyota = Car("Toyota", "Rav4", "2021", "black", 20000)
# #
# # print(toyota.check_engine())
# # print(toyota.start_engine())
# # print(toyota.stop_engine())
# # print(toyota.drive())
# # toyota.crush(1000)
# # print(toyota.price)
# # toyota.repair(2000)
# # print(toyota.price)
# # print(toyota.actions)
#
# class Student:
#     def __init__(self, first_name, last_name, grade):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.grade = grade
#         self.marks = []
#         self.courses = []
#         self.actions = []
#
#
#     def add_mark(self, mark: int):
#         self.marks.append(mark)
#         self.actions.append(f"{self.first_name} get {mark}")
#
#     def add_course(self, course_name):
#         self.courses.append(course_name)
#         self.actions.append(f"{self.first_name} go to {course_name}")
#
#     def leave_course(self, course_name):
#         self.courses.remove(course_name)
#         self.actions.append(f"{self.first_name} leave from {course_name}")
#
#     def get_average_mark(self):
#         average_mark = sum(self.marks) / len(self.marks)
#         if average_mark  >= 2 and average_mark <= 3:
#             return f"{self.first_name} is DVOECHNIK"
#         elif average_mark >= 4 and average_mark <= 5:
#             return f"{self.first_name} is UDARNIK"
#         elif average_mark >= 3 and average_mark <= 4:
#             return f"{self.first_name} is TROECHNIK"
#         elif average_mark > 4 and average_mark <= 5:
#             return f"{self.first_name} is OTLICHNIK"
#
#
# person_1 = Student("Timur", "Abdybekov", 9)
#
# person_1.add_mark(5)
# person_1.add_mark(3)
# print(person_1.get_average_mark())



class A:
    a = "sfsdfs"

    def __init__(self, x):
        self.x = x

    def set_x(self, x):
        self.x = x

    def get_x(self):
        return self.x

obj = A(5)
obj.set_x(10)
print(obj.get_x())












