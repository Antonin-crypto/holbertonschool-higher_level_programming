#!/usr/bin/python3
"""Definition of function my_list"""


class MyList(list):
    """Custom list class"""
    def print_sorted(self):
        """Prints the elements of the list in sorted order"""
        for element in self:
            if not isinstance(element, int):
                raise TypeError("not all the elements type int")
        print(sorted(self))
