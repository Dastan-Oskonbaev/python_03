import json
import requests

url = "https://api.kanye.rest"
count = 0

while count < 20:
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    if response.status_code == 200:
        content = json.loads(response.text)
        if content:
            with open('quotes.txt', 'r') as f:
                f.readlines()
                if content['quote'] in f.readlines():
                    continue
                with open('quotes.txt', 'a') as f:
                    f.write(content['quote'] + '\n')
                    count += 1

"""
Условие задачи:
Скачайте 50 уникальных цитат из API по адресу: https://api.kanye.rest.
Если цитата уже есть в файле quotes.txt, пропустите её и запросите новую цитату.
Если файл quotes.txt не существует, создайте его.
После выполнения программы файл quotes.txt должен содержать ровно 50 уникальных цитат.
"""
#Дополнительное задание :
# Добавьте обработку ошибок:


