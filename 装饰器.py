# def decorator_func(original_func):
# #     def wrapper_func(*args, **kwargs):
# #         # 在原函数前后执行一些操作
# #         print(args[0]+1)
# #         return original_func(*args, **kwargs)
# #     return wrapper_func
# #
# # def decorator_func2(original_func):
# #     def wrapper_func(*args, **kwargs):
# #         # 在原函数前后执行一些操作
# #         print(a+1)
# #         return original_func(*args, **kwargs)
# #     return wrapper_func
# #
# # a = 123
# # @decorator_func2
# # @decorator_func
# # def original_func(*args, **kwargs):
# #     pass
# #
# # original_func(a)

import csv

data = [
    ['Name', 'Age', 'City'],
    ['John', 25, 'New York'],
    ['Alice', 30, 'London'],
    ['Bob', 35, 'Paris']
]

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)