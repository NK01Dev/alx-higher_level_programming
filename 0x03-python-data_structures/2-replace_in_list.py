#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return None
    elif len(my_list) - 1 < idx:
        return None
    else:
        my_list[idx] = element
        return my_list

