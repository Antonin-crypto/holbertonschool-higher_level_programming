#!/usr/bin/python3
"""Definition of function my_list"""


class MyList(list):
    """Custom list class"""
    def print_sorted(self):
        """Prints the elements of the list in sorted order"""
        sorted_list = sorted(self)
        print(sorted_list)
