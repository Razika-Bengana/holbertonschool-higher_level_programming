#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_copy = my_list.copy()
    for i in range(len(my_list)):
        if (my_list[i] % 2 == 0):
            list_copy[i] = True
        else:
            list_copy[i] = False
            return (list_copy)
