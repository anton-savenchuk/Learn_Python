# from enum import unique
# import time

# start = time.perf_counter()
# print()


#######################################################################
# Напишите функцию friends, которая из списка пар друзей сделает
# словарь, в котором каждому человеку будет сопоставлено множество
# его друзей.

# friends([("Ivan", "Maria"), 
#          ("Ella", "Ivan"), 
#          ("Ivan", "Oleg")]) == \
# {"Ivan":{"Maria", "Ella", "Oleg"},
#  "Ella":{"Ivan"},
#  "Maria": {"Ivan"},
#  "Oleg": {"Ivan"}}

# names = [("Ivan", "Maria"),
#          ("Ella", "Ivan"),
#          ("Ivan", "Oleg")]

# def friends(pairs):
#     friends_dict = {}
#     for pair in pairs:
#         name, friend_name = pair
#         friends_dict[name] = set(friends_dict.get(name, set())) | {friend_name}
#         friends_dict[friend_name] = set(friends_dict.get(friend_name, set())) | {name}

#     return friends_dict


# print(friends(names))


#######################################################################
# Генераторы (comprehensions)

# Напишите код, который в переменной a создаст список натуральных чисел
# от 1 до 2000 включительно.
# a = [i for i in range(1, 2001)]


# Напишите код, который в переменной a создаст список чисел от 1 до
# 10000 делящихся на 3
# a = [i for i in range(1, 10001) if i % 3 == 0]


# Напишите код, который прочитает строчку целых чисел разделенных
# пробелом и положит список этих чисел в переменную a
# a = [int(i) for i in input().split()]


# Напишите код, который прочитает строчку целых чисел разделенных
# пробелом и создаст в переменной a список квадратов этих чисел в
# переменную a
# a = [int(i) ** 2 for i in input().split()]


# print()
# print(time.perf_counter() - start)
