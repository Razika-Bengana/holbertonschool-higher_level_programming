#!/usr/bin/python3

if __name__ == "__main__":

    import hidden_4

    comp_names = dir(hidden_4)

    for name in comp_names:

        if comp_names[:2] != "__":
            print(comp_names)
