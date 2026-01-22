#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    count = 0
    for x in my_list:
        count += 1
    if idx >= count:
        return my_list
    my_list[idx] = element
    return my_list
