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

names = [("Ivan", "Maria"),
            ("Ella", "Ivan"),
            ("Ivan", "Oleg")]

def friends(pairs):
    friends_dict = {}
    for pair in pairs:
        name, friend_name = pair
        friends_dict[name] = set(friends_dict.get(name, set())) | {friend_name}
        friends_dict[friend_name] = set(friends_dict.get(friend_name, set())) | {name}

    return friends_dict


print(friends(names))


# print()
# print(time.perf_counter() - start)
