# list comrehentions
# генераторы списков

# number_list = []
# for i in range(1, 1001):
#     number_list.append(i)
# print(number_list)
# number_list = [i for i in range(1,1001) if i % 2 == 0]
# print(number_list)
# list = ["aplle", "banana", "cherry", "peach"]
# new_fruits = [fruit for fruit in list]
# print(new_fruits)
# list = ["aplle", "banana", "cherry", "peach"]
# new_fruits = [fruit[:3] if fruit != "banana" else "potato"[:4] for fruit in list]
# print(new_fruits)

# number_list = [i if i % 100 == 0 else "Null" for i in range(1,1001) if i % 2 == 0]
# print(number_list)
# numbers_id = [ord(i.upper()) for i in "Python"]
# print(numbers_id)
# chars = [chr(i) for i in numbers_id]
# print("".join(chars))

# from datetime import timedelta, datetime
# before = datetime.now()
# # print(now)
# # now = datetime.now()
# lists = []
# for i in range(1, 1001):
#     lists.append(i)
# # number_list = [i for i in range(1, 10001)]
# delta = datetime.now() - before
# print(delta)
#git

# task of dict
# dictonary = {}
# dict_one = {"Posl": 2, "Posl2": 4, "Pos3": 4 }
# dict_two = {"Pos": 3, "Pos1": 3, "Pos3": 3}
# dict_three = {"Post": 4}
# dict_one1 = list(dict_one)
# for key, value in dict_one.items():
#     dictonary.update([key][value])
#
# print(dictonary)
# dict_two = list(dict_two)
# dict_three = list(dict_three)
# dictonary = dict_one + dict_two + dict_three
# dictonary = (dict_three | dict_two )
# dictonary = (dict_one | dictonary)
# return( dictonary)
# dictonary = (dict_three | dict_two)
# print( dictonary)

# polindrom
# k = input("Point your word")
# print(k)
# d = k[::-1]
# print(d)
# if k == d:
#     print("polindrom")
# else:
#     print("ne polindrom")

# tuple task
# arr = [4, 7, 16, 17, 0, 4]
# # i if i % 100 == 0 else "Null" for i in arr if i % 2 == 0
# for i in range(0, len(arr)):
#     k = False
#     for j in range (0, len(arr)):
#         print(arr[i], arr[j])
#         if arr[i] == arr[j] * 2  and i != j:
#             print("hello")
#             k = True
#             break
#     if k == True:
#         break
#
#
# print(k)

# str task
# filename = 'jdhfjdhhj.jpeg'
# s = filename.split('.')
# print(s)
# if s[1] == 'png':
#     return 'Расширение файла - png'
# elif s[1] == 'doc':
#     return 'Расширение файла - doc'
# elif n[1] == 'jpeg':
#     return 'Расширение файла - jpeg'
# elif n[1] == 'xlsx':
#     return 'Расширение файла - xlsx'
# elif n[1] == 'html':
#     return 'Расширение файла - html'
first_list = [96, 41, 6, 31, 6, 96, 'ret', 3]
second_list = [96, 6]
# #midl = a.count(3)
# print(f'First {a[:1]} , Second {a[int(len(a) / 2)]} Three {a[-1:]}' )
# # print(midl)
general = []
for i in first_list:
    for j in second_list:
        if i == j:
            if i not in general:
                general.append(i)
                break
print(general)