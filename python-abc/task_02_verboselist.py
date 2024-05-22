#!/usr/bin/env python3

class VerboseList(list):
    def append(self, item):
        super().append(item)
        print("Added {} to the list.".format([item]))

    def extend(self, iterable):
        super().extend(iterable)
        num_items = len(iterable)
        print("Extended the list with {} items.".format([num_items]))

    def remove(self, item):
        try:
            super().remove(item)
            print("Removed {} from the list.".format([item]))
        except ValueError:
            print("{} not found in the list.".format([item]))

    def pop(self, index=None):
        if index is None:
            item = super().pop()
        else:
            item = super().pop(index)
        print("Popped {} from the list.".format([item]))
