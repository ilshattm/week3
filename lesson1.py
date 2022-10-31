# dict slovari
#{"key": "value"}
# dicts = {
#     "name": "Ilshat",
#     "age": 13,
#     "subject":{
#         "python": 67,
#         "math": 80,
#     },
#     "shools":{
#         "68": 2001,
#         "13":2005,
#     }
#
# }
#print(dicts["subject"]["python"])
# for i in dicts:
#     if type(dicts[i]) == dict:
#         for j in dicts[i]:
#             print(dicts[i][j])
#  python = {
#       "redl": 34,
#      "bred": 373,
#      "redkq": 83,
#      "sred": 69,
#      "ared": 65,
#      "ered": 23,
#  }
# python["dorn"] = 100, 83
# print(python)
# print(python.keys())
# print(python.values())


# for i, j in python.items():
#     print(i, j)
# python = {
#       "redl": 34,
#      "bred": 373,
#      "redkq": 83,
#      "sred": 69,
#      "ared": 65,
#      "ered": 23,
#  }
# python. clear()
# print(python)
# print(sum(python.values()) / len(python))
# sum = 0
# for values in python.values():
#     sum = sum + values
# average = sum / len(python)
# dicys = dict()
# #print(type(dicys))
# print(average)
# ared = python.pop("ared")
# print(ared)
# print(python)
# ared = python.popitem()
# print(ared)
# print(python)
# languages = ["python", "java", "go"]
# dict_languages = dict.fromkeys(languages)
# print(dict_languages)
# python = {
#       "redl": 34,
#      "bred": 373,
#      "redkq": 83,
#      "sred": 69,
#      "ared": 65,
#      "ered": 23,
#  }
# dict_product = {}
# while True:
#     a = input("Input name and price of food: ")
#     if a == 'stop':
#         print(dict_product)
#         a = input("Input start for continue: ")
#         if a == 'start':
#             continue
#     key, value = a.split()
#     dict_product[key] = int(value)/83
# numbers_list = [1, 3, -4, 65, -34, -23, 23]
# numbers_list1 = []
# numbers_list2 = []
# k = 0
# for i in numbers_list:
#     if i < 0:
#         numbers_list1.append(i)
#     else:
#         numbers_list2.append(i)
# numbers_list1 = tuple(numbers_list1)
# numbers_list2 = tuple(numbers_list2)
# print(numbers_list1)
# print(numbers_list2)
from copy import deepcopy
# student = {
#     "name": "Ilsh",
#     "surname": "shat",
#     "subject": [
#         {"name": "math", "grade": 80},
#         {"name": "programing", "grade": 100}
#     ]
# }
# print(student)
# student2 = student.copy()
# print(student.get('subject'))
# print(student.items())
# print(student2)
a = "".join("1")
print(a)