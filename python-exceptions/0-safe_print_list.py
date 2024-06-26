#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for index in range(x):
            print(my_list[index], end="")
            count += 1
    except IndexError:
        pass
    finally:
        print()
        return count
