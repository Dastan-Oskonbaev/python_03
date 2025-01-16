from urllib import response, request

import requests

# file = open("dogs.txt", "w")
# file.writelines("Hello World")
# file.writelines("Bye Bye")
# file.close()

# file = open("my_file.txt", "r")
# content = file.read()
# print(content)
# file.close()

# file = open("my_file.txt", "r")
# content = file.readlines()
# file.close()
#
# print(content)
#
# file_2 = open("my_file_2.txt", "a")
# for i in content:
#     word = i.rstrip('\n')
#     file_2.writelines(word)
# file_2.close()


# with open("my_file.txt", "r") as f:
#     content = f.readlines()
#     print(content)
#
#     with open("my_file_3.txt", "w") as file:
#         for i in content:
#             word = i.rstrip('\n')
#             file.write(word)


# with open("numbers.txt", "w") as f:
#     for i in range(1, 101):
#         f.writelines((str(i) + "\n"))


# with open("numbers.txt", "r") as f:
#     numbers = f.readlines()
#     for i in numbers:
#         num = i.rstrip('\n')
#         if int(num) % 3 == 0:
#             with open("numbers_2.txt", "a") as f_2:
#                 f_2.write(num + "\n")

# with open("numbers_2.txt", "r") as f:
#     subcategory_ids = f.readlines()
#
# query = "INSERT INTO \"app\".\"subcategory_price\" (\"id\", \"subcategory_id\", \"price\") VALUES\n"
# values = []
#
# for subcategory_id in subcategory_ids:
#     values.append(f"(gen_random_uuid(), '{subcategory_id}', 0)")
#
# query += ",\n".join(values) + ";"
#
# print(query)

# my_list = [i for i in range(20)]
# print(f"LIST: {my_list}")

# oven_nums = [i for i in my_list if i % 2 == 0]
# print(f"OVENS: {oven_nums}")
#
# squares = [i**2 for i in oven_nums]
# print(f"Squares: {squares}")

# x = lambda x: x ** 3
# print(x(5))

# y = lambda x, y: x + y
# print(y(1, 2))

# my_filter = list(filter(lambda i: i % 2 == 0, my_list))
#
# def my_func(x):
#     if x % 2 == 0:
#         return x
#
# my_filter_2 = list(filter(my_func, my_list))
#
# print(f"my_filter: {my_filter}")
# print(f"my_filter_2: {my_filter_2}")


# my_map = list(map(lambda x: x **3, my_list))
# print(f"MAP: {my_map}")


# def my_func(*args, **kwargs):
#     if args:
#         return sum(args)
#     return sum(kwargs.values())
#
# print(my_func(1, 2, 3))
# print(my_func(a=1, b=2, c=3))
import math

# def calculate(*args, **kwargs):
#     operation = kwargs.get("operation")
#     if operation == "sum":
#         return sum(args)
#     elif operation == "multiply":
#         result = 1
#         for i in args:
#             result *= i
#         return result
#
# print(calculate(1, 2, 3, operation="sum"))
# print(calculate(1, 2, 3, 4, operation="multiply"))



# my_dict = {}
# for k in range(10):
#     my_dict[k] = k ** 2
#
# print(my_dict)