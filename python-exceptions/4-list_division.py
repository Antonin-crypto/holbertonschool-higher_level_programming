#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for idx in range(0, list_length):
        try:
            result.append(my_list_1[idx] / my_list_2[idx])
        # element is not an integer or float:
        except TypeError:
            print("wrong type")
            result.append(0)
        # the division can’t be done (/0):
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        # If my_list_1 or my_list_2 is too short
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            pass
    return result
