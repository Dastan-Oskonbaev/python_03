# class Animal:
#     def speak(self):
#         print("Animal speak")
#
#
# class Dog(Animal):
#     def speak(self):
#         print("Dog speak")
#
#
# class Cat(Animal):
#     def speak(self):
#         print("Cat speak")
#
# animal = Animal()
# dog = Dog()
# cat = Cat()
#
# animal.speak()
# dog.speak()
# cat.speak()


# class Tv:
#     def __init__(self, brand, price, size):
#         self.brand = brand
#         self._price = price
#         self.__size = size
#
#
# tv = Tv("Sony", 1000, 70)
# print(tv.brand)
# print(tv._price)
# print(tv._Tv__size)

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def get_product_name(self):
#         print(f"Product: {self.name}, price: {self.price}")
#
#
# class Food(Product):
#     def __init__(self, name, price, weight):
#         super().__init__(name, price)
#         self.__weight = weight
#
#     @property
#     def get_product_name(self):
#         return f"Food: {self.name}"
#
#     @property
#     def weight(self):
#         return self.__weight
#
#
# class Electronic(Product):
#     def __init__(self, name, price, color, size, screen_size):
#         super().__init__(name, price)
#         self._color = color
#         self.__size = size
#         self.screen_size = screen_size
#
#
#     def get_product_name(self):
#         return f"Electronic: {self.name}, color: {self._color}, size: {self.__size}"
#
#     @property
#     def size(self):
#         return self.__size
#
#     @size.setter
#     def size(self, value):
#         self.__size = value


# phone = Electronic("phone", 500, "Blue", 15)
# phone.set_size = 20
# print(phone.size)

# class Person:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#     @property
#     def name(self):
#         return self._name
#     @property
#     def age(self):
#         return self._age // 12  # возвращаем возраст в годах
#     @age.setter
#     def age(self, value):
#         if value < 0:
#             value = 0
#         elif value > 150:
#             value = 150
#         self._age = value * 12
#
#
# person = Person("Aga", 60)
# print(person.age)
# person.age = 25
# print(person.age)

# from abc import ABC, abstractmethod
#
#
# class Person(ABC):
#     def __init__(self, name, surname, age, email):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.email = email
#
#     @abstractmethod
#     def greet(self):
#         pass
#
#
# class Student(Person):
#     def __init__(self, name, surname, age, email, grade):
#         super().__init__(name, surname, age, email)
#         self.grade = grade
#         self.grades = []


# class Math:
#     @staticmethod
#     def add(a, b):
#         return a + b
#
#
# math = Math()
# print(math.add(5, 5))
# print(Math.add(2, 3))

# from datetime import datetime
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
#     @classmethod
#     def birth_from_year(cls, name, year):
#         current_year = datetime.now().year
#         age = current_year - year
#         return cls(name, age)
#
# p = Person.birth_from_year("Pudge", 1999)
# print(p.name, p.age)


# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     @classmethod
#     def return_in_som(cls, name, price):
#         usd_price = 86.8
#         price = price * usd_price
#         return cls(name, price)
#
#
# product = Product.return_in_som('Milk', 100)
# print(product.name, product.price)


import requests
from bs4 import BeautifulSoup

# URL сайта, который будем парсить
url = "https://new.technodom.kg/category/noutbuki-i-komp-jutery"

# Отправляем GET-запрос
response = requests.get(url)

# Проверяем статус ответа
if response.status_code == 200:
    # Создаем объект BeautifulSoup
    soup = BeautifulSoup(response.text, "lxml")
    # Находим все заголовки <h1>
    headers = soup.find_all("div", class_="common__recommendations__list__item one-five")
    print(headers)
    # Выводим текст заголовков
    for header in headers:
        print(header.text.strip())
else:
    print(f"Не удалось загрузить страницу, статус: {response.status_code}")







