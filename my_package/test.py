"""
Условие задачи:
Скачайте 50 уникальных цитат из API по адресу: https://api.kanye.rest.
Если цитата уже есть в файле quotes.txt, пропустите её и запросите новую цитату.
Если файл quotes.txt не существует, создайте его.
После выполнения программы файл quotes.txt должен содержать ровно 50 уникальных цитат.
"""
# Дополнительные задания:
# Добавьте обработку ошибок
# В терминале: pip install requests

# import requests
# import json
#
#
# try:
#     while True:
#         url = "https://api.kanye.rest"
#         response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
#         if response.status_code == 200:
#             content = json.loads(response.text)
#             if content:
#                 with open('quotes.txt', 'r') as f:
#                     a = f.readlines()
#                     if content in a:
#                         continue
#                     elif len(a) > 50:
#                         break
#                     else:
#                         with open('quotes.txt', 'a') as f:
#                             f.write(content['quote'] + '\n')
# except Exception as e:
#     print(e)
