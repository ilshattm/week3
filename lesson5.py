# #function
# def get_sum():
#     print(2 + 4)
# a = get_sum()
# print/(a)
#####################################
# def get_circle_square():
#     r  = 16
#     s = 3.14 * r ** 2
#     return s, r
# square, rad = get_circle_square()
# print(square)
# print(rad)

####################################
# money = int(input("Input money"))
# year = int(input("Input count"))
# PROCENT = 0.1
# count_money = money * PROCENT *year + money
# print(count_money)

# def result_vklad(money: int, year: int) -> float:
#     PROCENT = 0.1
#     count_money = money * PROCENT * year + money
#     return count_money
# print(result_vklad(year=money, money=year))
##########################################################
# *args, **kwargs
# def get_kwargs_args(*args, **kwargs):
#     if args:
#         print(args)
#     if kwargs:
#         print(kwargs)
#     print("retro")
# get_kwargs_args(1, "Flat", 2, "Rent", age=35, name='Kapa')
##########################################################
def result_generate_time(*args):
    from datetime import timedelta, datetime
    before = datetime.now()
    number_list = [i for i in range(1,10000)]
    if args and len(args) == 1:
        number_list = [i for i in range(1, args[0])]
    elif args and len(args) == 2:
        number_list = [i for i in range(1, args[0], args[1])]
    delta = datetime.now() - before
    return delta, number_list

print(result_generate_time(1000, 4))