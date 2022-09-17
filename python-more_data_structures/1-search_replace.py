#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for i in range(0, len(new_list)):
        new_list = [replace if new_list[i] == search else new_list[i]
                    for new_list[i] in new_list]
        return (new_list)
