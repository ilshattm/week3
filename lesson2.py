#set collections
# sets = set()
# print(type(sets))
# profession = {"backend", 12, (1, 2)}
#print(profession)
# cities = {"Tokyo", "Bishkek", "Baku", "Karakol"}
# towns = {"Bart", "Vill", "Nimen", "Bakuf"}
# print(cities.issubset(towns))
# towns.update(("Herka",))
# print(towns)
# print(cities.isdisjoint(towns))

# print(dir(cities))
# print(cities)
# cities.add("Norv")
# print(cities)
# a = cities.copy()
# print(a)
# cities.discard("Tokyo")
# cities.remove()
# print(cities)
# city_town = cities.union(towns)
# cities.update(towns)
# print(city_town)
# print(cities)

# cities.intersection_update(towns)
# print(cities)
# print(cities.symmetric_difference(towns))
# cities.symmetric_difference_update(towns)
# print(towns)
# print(cities)
# d = cities.pop()
# print(cities)
# print(d)

# stud = {
#     "name": "Ilsh",
#     "age": 39,
#     "year": None,
#     "subject": {
#         "math": (80, 36, 84, 100),
#         "go": (80, 37, 28, 45),
#         "rust": (20, 47, 38, 70),
#         "css": (54, 67, 52, 76)
#     },
#     "total": None
# }
# print(stud)
# print(years)
# stud["year"] = 2022 - stud["age"]
# print(stud)
# for i in stud:
#
#     if type(stud[i]) == dict:
#         print(stud[i])
#         k = 0
#         d = 0
#         for j in stud[i]:
#             k += stud[i][j]
#             d += 1
#         aver = k / d
# find average
# for key, value in stud['subject'].items():
#     stud['sub']
numbers = [1, 4, 4, 4, 4, 2, 3, 3, 3, 5, 5]
max = 1
for i in numbers:
    if max < numbers.count(i):
        max = numbers.count(i)
        maxim = i

print(maxim)
