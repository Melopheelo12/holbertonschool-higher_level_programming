#!/usr/bin/python3
def max_integer(my_list=[]):

    if len(my_list) == 0:
        return None

    max_num = my_list[0]
    for n in my_list:
        if n > max_num:
            max_num = n
    return max_num
