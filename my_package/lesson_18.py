# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print("I AM SOME ANIMAL")
#
# class Dog(Animal):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age
#
#     def speak(self):
#         print("NOW I AM A DOG")
#
# animal = Animal("animal")
# animal.speak()
#
# dog = Dog("dog", 3)
# dog.speak()


# class Technique:
#     def __init__(self, brand, size, color):
#         self.brand = brand
#         self.size = size
#         self.color = color
#
#     def work(self):
#         print("I'm working")
#
#     def not_work(self):
#         print("I'm not working")
#
#
# class Television(Technique):
#     def __init__(self, brand, size, color, model, scree_size):
#         super().__init__(brand, size, color)
#         self.model = model
#         self.scree_size = scree_size
#
#     def work(self):
#         print("I'm showing something")
#
#
# class Phone(Technique):
#     def __init__(self, brand, size, color, model, price):
#         super().__init__(brand, size, color)
#         self.model = model
#         self.price = price
#
#     def work(self):
#         print("I'm calling")
#
#     def introducing_music(self):
#         print("I'm introducing")
#
#
# class Microwave(Technique):
#     def __init__(self, brand, size, color, model, timer):
#         super().__init__(brand, size, color)
#         self.model = model
#         self.timer = timer
#
#     def work(self):
#         print("I'm warming food")

# from builtins import BaseException
#
#
# class Agahanexception(BaseException):
#     def __init__(self, message="Это личная ошибка Агахана"):
#         super(Agahanexception, self).__init__(message
#         )
#
#
#
# class Bird:
#     def __init__(self, name):
#         self.name = name
#
#     def fly(self):
#         print("I'm flying")
#
# class Sparrow(Bird):
#
#     def let_fly(self):
#         self.fly()
#
#
# class Penguin(Bird):
#     def let_fly(self):
#        raise Agahanexception()
#
# # sparrow = Sparrow("sparrow")
# # sparrow.fly()
# # sparrow.let_fly()
#
# penguin = Penguin("Penguin")
# penguin.let_fly()


km = float(input('введите растояние в километрах:'))


def road(kilometrs):
    kilometrs_k = kilometrs * 1000
    per_eache_140m = 0.25
    total = 4

    kilometrs = ((kilometrs_k / 140) * per_eache_140m + total)
    result = kilometrs

    print(result)


print(road(km))

