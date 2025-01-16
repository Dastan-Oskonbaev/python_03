# import requests
# from bs4 import BeautifulSoup
#
# class Product:
#     def __init__(self, name, price, img_url):
#         self.name = name
#         self.price = price
#         self.img_url = img_url
#
#
#     @classmethod
#     def from_soup(cls, name, price, img_url):
#         return cls(name, price, img_url)
#
#     def __str__(self):
#         return f"{self.name}, {self.price}, {self.img_url}"
#
# url = "https://new.technodom.kg/category/fototehnika-i-kvadrokoptery"
#
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "lxml")
#
# products = soup.find_all("div", class_="common__recommendations__list__item one-four")
# for product in products:
#     name = product.find("div", class_="common__recommendations__list__item__title").text
#     price = product.find("div", class_="common__recommendations__list__item__price").text
#     image = product.find("a")["data-background-image"]
#     p = Product.from_soup(name, price, image)
#     with open("products.txt", "a", encoding="utf-8") as f:
#         f.write(p.__str__() + '\n')


import requests
from bs4 import BeautifulSoup


class Currency:
    """Класс для представления валюты."""

    def __init__(self, name, rate):
        self.name = name
        self.rate = rate

    def __str__(self):
        """Магический метод для строкового представления."""
        return f"{self.name}: {self.rate}"


def fetch_currency_data(url):
    """Функция для загрузки HTML-страницы."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Ошибка загрузки страницы: {response.status_code}")


def parse_currency_data(html):
    """Функция для парсинга данных о валютах."""
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table", class_="ratesTable")
    rows = table.find_all("tr")[1:]  # Пропускаем заголовок таблицы

    currencies = []
    for row in rows:
        cols = row.find_all("td")
        name = cols[0].text.strip()
        rate = cols[1].text.strip()
        currencies.append(Currency(name, rate))
    return currencies


def save_to_file(currencies, filename):
    """Функция для записи данных в файл."""
    with open(filename, "w", encoding="utf-8") as file:
        for currency in currencies:
            file.write(str(currency) + "\n")


# Основной код
if __name__ == "__main__":
    url = "https://www.x-rates.com/table/?from=USD&amount=1"

    # Шаг 1: Загрузка HTML-страницы
    html = fetch_currency_data(url)

    # Шаг 2: Парсинг данных
    currencies = parse_currency_data(html)

    # Шаг 3: Сохранение данных в файл
    save_to_file(currencies, "currencies.txt")

    print("Данные успешно сохранены в файл 'currencies.txt'.")


