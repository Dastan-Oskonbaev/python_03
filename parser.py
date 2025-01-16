# class Car:
#     def __init__(self, name, color, speed):
#         self.name = name
#         self.color = color
#         self.speed = speed
#
#     def __str__(self):
#         return f'Name: {self.name}, color: {self.color}, speed: {self.speed}'
#
#
# car = Car("Supra", color="blue", speed=100)
# print(car)

# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def __str__(self):
#         return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"
#
#     def __len__(self):
#         return self.pages
#
#     def __eq__(self, other):
#         return self.pages == other.pages
#
#
#     def __gt__(self, other):
#         return self.pages > other.pages
#
#     def __lt__(self, other):
#         return self.pages < other.pages
#
#     def __ge__(self, other):
#         return self.pages >= other.pages
#
#     def __le__(self, other):
#         return self.pages <= other.pages
#
#
#
#
#
# obj = Book("One Punchman", "Anime Jakadzaki", 500)
# obj2 = Book("Kyzyl Alma", "Chyngyz Aitmatov", 1000)
# print(obj + obj2)
# print(obj)
#
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'({self.x}, {self.y})'
#
#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)
#
#     def __mul__(self, other):
#         return Point(self.x * other, self.y * other)
#
#     def __div__(self, other):
#         return Point(self.x / other, self.y / other)
#
#
# obj = Point(1, 2)
# obj2 = Point(5, 5)
# print(obj + obj2)


# import requests
# from bs4 import BeautifulSoup
#
# while True:
#     url = "https://new.technodom.kg/category/mebel-i-domashnij-inter-er"
#     response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
#     soup = BeautifulSoup(response.content, "lxml")
#     products = soup.find_all("div", class_="common__recommendations__list__item one-four")
#     for product in products:
#         name = product.find("div", class_="common__recommendations__list__item__title").text
#         price = product.find("div", class_="common__recommendations__list__item__price").text
#         image = product.find("a")['data-background-image']
#         print(name)
#         print(price)
#         print(image)


# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# url = "https://www.tazabek.kg/lenta"
# driver = webdriver.Chrome()
# driver.get(url)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# elements = driver.find_elements(By.XPATH,"//div[@class='lenta-row']")
# for element in elements:
#     list_1 = element.text.split("\n")
#     time = list_1[0]
#     title_split = list_1[1].split("\xad")
#     title = title_split[0]
#     views = title_split[1]
#     print(time)
#     print(title)
#     print(views)
#
# driver.quit()

#
# import requests
# from bs4 import BeautifulSoup
#
#
# url = "https://manascinema.com"
# response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
# soup = BeautifulSoup(response.content, "lxml")
# films = soup.find_all("div", class_="creation-wrapper")
# for film in films:
#     title = film.find("div", class_="creation-title").text
#     info = film.find("div", class_="creation-info").text
#     picture_relative = film.find("img")['src']
#     picture_absolute = url + picture_relative
#     print(title)
#     print(info)
#     print(picture_absolute)





"""
Спарсить курсы валют с сайта, например, https://www.x-rates.com/.
Использовать ООП: создать класс для работы с валютами.
Реализовать каждое действие (парсинг, обработка данных, запись в файл)
как независимое действие.
"""
# import requests
# from bs4 import BeautifulSoup
#
# class Rate:
#     def __init__(self, name, rate):
#         self.name = name
#         self.rate = rate
#
#     def __str__(self):
#         return f"{self.name} ({self.rate})"
#
#     @classmethod
#     def rates(cls, name, rate):
#         return cls(name, rate)
#
#
# url = "https://valuta.kg/"
# response = requests.get(url)
# soup = BeautifulSoup(response.content, "lxml")
# title = soup.find_all("div", class_="kurs-bar__rates")
# for item in title:
#     name = item.find("tbody").text.split("\n")
#     prices = item.find("div", class_="kurs-bar__item kurs-bar__item--nbkr")
#     price = prices.find("tbody").text.split("\n")
#     with open("ppp.txt", "a") as f:
#         a = Rate.rates(name, price)
#         f.write(str(a) + "\n")



# import requests
# from bs4 import BeautifulSoup
# import csv
#
#
# class Scraper:
#     def __init__(self, url):
#         self._url = url
#         self._html = None
#
#     def fetch(self):
#         response = requests.get(self._url)
#         if response.status_code == 200:
#             self._html = response.text
#         else:
#             raise Exception(f"Ошибка при загрузке страницы: {response.status_code}")
#
#     def parse(self):
#         raise NotImplementedError("Метод parse должен быть реализован в дочернем классе")
#
#
# class Product:
#     def __init__(self, name, price, description):
#         self.__name = name
#         self.__price = price
#         self.__description = description
#
#     def to_dict(self):
#         return {
#             "Название": self.__name,
#             "Цена": self.__price,
#             "Описание": self.__description,
#         }
#
#     @staticmethod
#     def validate_price(price):
#         return isinstance(price, (int, float)) and price > 0
#
#     @classmethod
#     def from_dict(cls, data):
#         return cls(data["Название"], data["Цена"], data["Описание"])
#
#
# class ProductScraper(Scraper):
#     def __init__(self, url):
#         super().__init__(url)
#         self.products = []
#
#     def parse(self):
#         if not self._html:
#             raise Exception("HTML-контент не загружен. Используйте метод fetch.")
#
#         soup = BeautifulSoup(self._html, "lxml")
#         items = soup.find_all("article", class_="product_pod")
#
#         for item in items:
#             name = item.h3.a["title"]
#             raw_price = item.find("p", class_="price_color").text.strip()
#             price = float(raw_price.replace('£', '').replace('Â', '').strip())
#             description = "Описание отсутствует"
#
#             if Product.validate_price(price):
#                 product = Product(name, price, description)
#                 self.products.append(product)
#
#     def save_to_csv(self, filename):
#         with open(filename, mode="w", encoding="utf-8", newline="") as file:
#             writer = csv.DictWriter(file, fieldnames=["Название", "Цена", "Описание"])
#             writer.writeheader()
#             for product in self.products:
#                 writer.writerow(product.to_dict())
#
#
# if __name__ == "__main__":
#     url = "https://books.toscrape.com/"
#     scraper = ProductScraper(url)
#
#     scraper.fetch()
#     scraper.parse()
#     scraper.save_to_csv("products.csv")
#
#     print("Данные успешно сохранены в файл 'products.cfsv'.")


sdfgbfdgbvdsfvjdnfvbjs
вфпавапапра
