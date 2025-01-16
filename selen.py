# import requests
# from bs4 import BeautifulSoup
#
# url = "https://manascinema.com"
#
# response = requests.get(url)
# soup = BeautifulSoup(response.content, "lxml")
#
# films = soup.find_all("div", class_="creation-wrapper")
#
# for film in films:
#     title = film.find("div", class_="creation-title").text
#     info = film.find("div", class_="creation-info").text
#     picture_hash = film.find("img")['src']
#     picture = url + picture_hash

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
#
# url = "https://www.tazabek.kg/lenta"
# # chrome_options = Options()
# # chrome_options.add_argument("--headless")
# driver = webdriver.Chrome()
# driver.get(url)
# elements = driver.find_elements(By.XPATH, "//div[@class='lenta-row']")
# for element in elements:
#     my_list = element.text.split("\n")
#     time = my_list[0]
#     title_and_views = my_list[1].split("\xad")
#     title = title_and_views[0]
#     views = title_and_views[1]
#     print(time)
#     print(title)
#     print(views)
# driver.quit()


# import requests
# from bs4 import BeautifulSoup
#
# url = "https://www.tazabek.kg/lenta"
# response = requests.get(url)
# soup = BeautifulSoup(response.content, "lxml")
# articles = soup.find_all("div", class_="lenta-row")
# for article in articles:
#     time = article.find("div", class_="lenta-row-date")
#     if time is not None:
#         print(f" Time {time.text}")
#         title = article.find("div", class_="lenta-row-title")
#         print(f"Статья: {title.text}")


# import requests
# from bs4 import BeautifulSoup
# import csv
#
#
# class Scraper:
#     """Базовый класс для работы с веб-страницами."""
#
#     def __init__(self, url):
#         self._url = url
#         self._html = None
#
#     def fetch(self):
#         """Загружает HTML-контент с указанного URL."""
#         response = requests.get(self._url)
#         if response.status_code == 200:
#             self._html = response.text
#         else:
#             raise Exception(f"Ошибка при загрузке страницы: {response.status_code}")
#
#     def parse(self):
#         """Метод для парсинга данных. Должен быть переопределен в наследниках."""
#         raise NotImplementedError("Метод parse должен быть реализован в дочернем классе")
#
#
# class Product:
#     """Класс для представления продукта."""
#
#     def __init__(self, name, price, description):
#         self.__name = name
#         self.__price = price
#         self.__description = description
#
#     def to_dict(self):
#         """Возвращает данные продукта в виде словаря."""
#         return {
#             "Название": self.__name,
#             "Цена": self.__price,
#             "Описание": self.__description,
#         }
#
#     @staticmethod
#     def validate_price(price):
#         """Проверяет корректность цены."""
#         return isinstance(price, (int, float)) and price > 0
#
#     @classmethod
#     def from_dict(cls, data):
#         """Создает экземпляр класса из словаря."""
#         return cls(data["Название"], data["Цена"], data["Описание"])
#
#
# class ProductScraper(Scraper):
#     """Класс для парсинга информации о продуктах."""
#
#     def __init__(self, url):
#         super().__init__(url)
#         self.products = []
#
#     def parse(self):
#         """Парсит данные о продуктах с HTML-страницы."""
#         if not self._html:
#             raise Exception("HTML-контент не загружен. Используйте метод fetch.")
#
#         soup = BeautifulSoup(self._html, "html.parser")
#         items = soup.find_all("article", class_="product_pod")
#
#         for item in items:
#             name = item.h3.a["title"]
#             raw_price = item.find("p", class_="price_color").text.strip()
#             price = float(raw_price.replace('£', '').replace('Â', '').strip())
#             description = "Описание отсутствует"  # В данном примере описание отсутствует на сайте
#
#             if Product.validate_price(price):
#                 product = Product(name, price, description)
#                 self.products.append(product)
#
#     def save_to_csv(self, filename):
#         """Сохраняет данные продуктов в CSV-файл."""
#         with open(filename, mode="w", encoding="utf-8", newline="") as file:
#             writer = csv.DictWriter(file, fieldnames=["Название", "Цена", "Описание"])
#             writer.writeheader()
#             for product in self.products:
#                 writer.writerow(product.to_dict())
#
#
# # Пример использования:
# if __name__ == "__main__":
#     url = "https://books.toscrape.com/"
#     scraper = ProductScraper(url)
#
#     scraper.fetch()  # Загружаем HTML
#     scraper.parse()  # Парсим продукты
#     scraper.save_to_csv("products.csv")  # Сохраняем в файл
#
#     print("Данные успешно сохранены в файл 'products.csv'.")



from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://www.tazabek.kg/lenta"
driver = webdriver.Chrome()
driver.get(url)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
elements = driver.find_elements(By.XPATH,"//div[@class='lenta-row']")

urls = []
for element in elements:
    url_element = element.find_element(By.XPATH, ".//a")
    urls.append(url_element.get_attribute("href"))
for link in urls:
    try:
        driver.get(link)
        time.sleep(2)

        title = driver.find_element(By.XPATH, "//h2[@class='title']").text
        article = driver.find_element(By.XPATH, "//div[@class='text']").text
        date_time = driver.find_element(By.XPATH, "//span[@class='date']").text

        with open("ppp.txt", "a") as file:
            file.write(f"URL: {link}\n")
            file.write(f"Time: {date_time}\n")
            file.write(f"Title: {title}\n")
            file.write(f"Article: {article}\n")
            file.write(("-" * 40)+ "\n")


    except Exception as e:
        print(f"Ошибка при парсинге URL {link}: {e}")

driver.quit()